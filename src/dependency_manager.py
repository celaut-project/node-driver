from time import sleep, time as time_now
from datetime import datetime, timedelta
from threading import Thread, Lock
from gateway_pb2_grpcbf import StartService_input_partitions, StartService_input
from utils import read_file
from grpcbigbuffer import Dir, client_grpc
import grpc

import api_pb2, api_pb2_grpc, gateway_pb2, gateway_pb2_grpc, solvers_dataset_pb2, celaut_pb2 as celaut
from singleton import Singleton
from start import DIR, LOGGER, SHA3_256, SHA3_256_ID, get_grpc_uri

# Si se toma una instancia, se debe de asegurar que, o bien se agrega a su cola
#  correspondiente, o bien se para. No asegurar esto ocasiona un bug importante
#  ya que las instancias quedarían zombies en la red hasta que el clasificador
#  fuera eliminado.

class ServiceInstance(object):
    def __init__(self, stub, token):
        self.stub = stub
        self.token = token
        self.creation_datetime = datetime.now()
        self.use_datetime = datetime.now()
        self.pass_timeout = 0
        self.failed_attempts = 0

    def error(self):
        sleep(1) # Wait if the solver is loading.
        self.failed_attempts = self.failed_attempts + 1

    def is_zombie(self,
                  SOLVER_PASS_TIMEOUT_TIMES,
                  TRAIN_SOLVERS_TIMEOUT,
                  SOLVER_FAILED_ATTEMPTS
                  ) -> bool:
        # En caso de que tarde en dar respuesta a cnf's reales,
        #  comprueba si la instancia sigue funcionando.
        return self.pass_timeout > SOLVER_PASS_TIMEOUT_TIMES and \
               not self.check_if_is_alive(timeout=TRAIN_SOLVERS_TIMEOUT) \
               or self.failed_attempts > SOLVER_FAILED_ATTEMPTS

    def timeout_passed(self):
        self.pass_timeout = self.pass_timeout + 1

    def reset_timers(self):
        self.pass_timeout = 0
        self.failed_attempts = 0

    def mark_time(self):
        self.use_datetime = datetime.now()

    def check_if_is_alive(self, timeout) -> bool:
        LOGGER('Check if instance ' + str(self.token) + ' is alive.')
        cnf = api_pb2.Cnf()
        clause = api_pb2.Clause()
        clause.literal.append(1)
        cnf.clause.append(clause)
        try:
            next(client_grpc(
                method = self.stub.Solve,
                input = cnf,
                indices_serializer = api_pb2.Cnf,
                timeout = timeout
            ))
            return True
        except (TimeoutError, grpc.RpcError):
            return False

    def stop(self, gateway_stub):
        LOGGER('Stops this instance with token ' + str(self.token))
        while True:
            try:
                next(client_grpc(
                    method = gateway_stub.StopService,
                    input = gateway_pb2.TokenMessage(
                                token = self.token
                            ),
                    indices_serializer = gateway_pb2.TokenMessage
                ))
                break
            except grpc.RpcError as e:
                LOGGER('GRPC ERROR STOPPING SOLVER ' + str(e))
                sleep(1)


class ServiceConfig(object):
    def __init__(self, service_with_config: solvers_dataset_pb2.SolverWithConfig, service_hash: str, stub_class):

        self.stub_class = stub_class

        self.solver_hash = service_hash  # SHA3-256 hash value that identifies the service definition on memory (if it's not complete is the hash of the incomplete definition).
        try:
            self.hashes = service_with_config.meta.hashtag.hash # list of hashes that the service's metadata has.
        except:  # if there are no hashes in the metadata
            if service_with_config.meta.complete: # if the service definition say that it's complete, the solver hash can be used.
                self.hashes = [celaut.Any.HashTag.hash(
                    type = SHA3_256_ID,
                    value = bytes.fromhex(service_hash)
                )]
            else:
                self.hashes = []

        # Service configuration.
        self.config = celaut.Configuration()
        self.config.enviroment_variables.update(service_with_config.enviroment_variables)

        # Service's instances.
        self.instances = []  # se da uso de una pila para que el 'maintainer' detecte las instancias que quedan en desuso,
        #  ya que quedarán estancadas al final de la pila.

    def service_extended(self):
        config = True
        for hash in self.hashes:
            if config:  # Solo hace falta enviar la configuracion en el primer paquete.
                config = False
                yield gateway_pb2.HashWithConfig(
                    hash = hash,
                    config = self.config
                )
            yield hash
        yield ( 
            gateway_pb2.ServiceWithMeta,
            Dir(DIR+'__solvers__/'+self.solver_hash+'/p1'),
            Dir(DIR+'__solvers__/'+self.solver_hash+'/p2')
        )

    def service_extended_from_disk(self):
        config = True
        for hash in self.hashes:
            if config:  # Solo hace falta enviar la configuracion en el primer paquete.
                config = False
                yield gateway_pb2.HashWithConfig(
                    hash = hash,
                    config = self.config,
                    min_sysreq = gateway_pb2.celaut__pb2.Sysresources(
                        mem_limit = 80*pow(10, 6)
                    )
                )
            yield hash
        while True:
            if not os.path.isfile(DIR + 'services.zip'):
                yield (gateway_pb2.ServiceWithMeta, Dir(DIR + 'regresion.service'))
                break
            else:
                sleep(1)
                continue

    def launch_instance(self, gateway_stub) -> ServiceInstance:
        LOGGER('    launching new instance for solver ' + self.solver_hash)
        while True:
            try:
                instance = next(client_grpc(
                    method = gateway_stub.StartService,
                    input = self.service_extended(),
                    indices_parser = gateway_pb2.Instance,
                    partitions_message_mode_parser=True,
                    indices_serializer = StartService_input,
                    partitions_serializer = StartService_input_partitions
                ))
                break
            except grpc.RpcError as e:
                LOGGER('GRPC ERROR LAUNCHING INSTANCE. ' + str(e))
                sleep(1)

        try:
            uri = get_grpc_uri(instance.instance)
        except Exception as e:
            LOGGER(str(e))
            raise e
        LOGGER('THE URI FOR THE SOLVER ' + self.solver_hash + ' is--> ' + str(uri))

        return ServiceInstance(
            stub = self.stub_class(
                    grpc.insecure_channel(
                        uri.ip + ':' + str(uri.port)
                    )
            ),
            token = instance.token
        )

    def add_instance(self, instance: ServiceInstance, deep=False):
        LOGGER('Add instance ' + str(instance))
        self.instances.append(instance) if not deep else self.instances.insert(0, instance)

    def get_instance(self, deep=False) -> ServiceInstance:
        LOGGER('Get an instance of. deep ' + str(deep))
        LOGGER('The solver ' + self.hashes[0].value.hex() + ' has ' + str(len(self.instances)) + ' instances.')
        try:
            return self.instances.pop() if not deep else self.instances.pop(0)
        except IndexError:
            LOGGER('    list empty --> ' + str(self.instances))
            raise IndexError
    
    def get_service_with_config(self) -> solvers_dataset_pb2.SolverWithConfig:
        solver_with_meta = api_pb2.ServiceWithMeta()
        solver_with_meta.ParseFromString(
            read_file(DIR + '__solvers__/' + self.solver_hash + '/p1')
        )
        solver_with_meta.ParseFromString(
            read_file(DIR + '__solvers__/' + self.solver_hash + '/p2')
        )
        return api_pb2.solvers__dataset__pb2.SolverWithConfig(
                    meta = solver_with_meta.meta,
                    definition = solver_with_meta.service,
                    config = self.config
                )


class Session(metaclass = Singleton):

    def __init__(self, ENVS: dict):

        # set used envs on variables.
        self.GATEWAY_MAIN_DIR = ENVS['GATEWAY_MAIN_DIR']
        self.SOLVER_PASS_TIMEOUT_TIMES = ENVS['SOLVER_PASS_TIMEOUT_TIMES']
        self.MAINTENANCE_SLEEP_TIME = ENVS['MAINTENANCE_SLEEP_TIME']
        self.SOLVER_FAILED_ATTEMPTS = ENVS['SOLVER_FAILED_ATTEMPTS']
        self.TRAIN_SOLVERS_TIMEOUT = ENVS['TRAIN_SOLVERS_TIMEOUT']
        self.MAX_DISUSE_TIME_FACTOR = ENVS['MAX_DISUSE_TIME_FACTOR']

        LOGGER('INIT SOLVE SESSION ....')
        self.solvers = {}
        self.gateway_stub = gateway_pb2_grpc.GatewayStub(grpc.insecure_channel(self.GATEWAY_MAIN_DIR))
        self.lock = Lock()
        Thread(target=self.maintenance, name='Maintainer').start()

    def maintenance(self):
        while True:
            sleep(self.MAINTENANCE_SLEEP_TIME)
            index = 0
            while True:  # Si hacemos for solver in solvers habría que bloquear el bucle entero.
                LOGGER('maintainer want solvers lock' + str(self.lock.locked()))
                self.lock.acquire()
                # Toma aqui el máximo tiempo de desuso para aprovechar el uso del lock.
                max_disuse_time = max(
                    len(self.solvers) * self.TRAIN_SOLVERS_TIMEOUT,
                    self.MAINTENANCE_SLEEP_TIME
                )
                try:
                    solver_config = self.solvers[
                        list(self.solvers)[index]
                    ]
                    index += 1
                    try:
                        instance = solver_config.get_instance(deep=True)

                        # Toma aqui el máximo tiempo de desuso para aprovechar el lock.
                        # Si salta una excepción la variable no vuelve a ser usada.
                        max_disuse_time = len(self.solvers) * self.TRAIN_SOLVERS_TIMEOUT * self.MAX_DISUSE_TIME_FACTOR
                    except IndexError:
                        # No hay instancias disponibles en esta cola.
                        self.lock.release()
                        continue
                except IndexError:
                    LOGGER('Se han recorrido todos los solvers.')
                    self.lock.release()
                    break
                except Exception as e:
                    LOGGER('ERROR on maintainer, ' + str(e))
                    self.lock.release()
                    break
                self.lock.release()

                LOGGER('      maintain solver instance --> ' + str(instance))
                # En caso de que lleve mas de demasiado tiempo sin usarse.
                # o se encuentre en estado 'zombie'
                if datetime.now() - instance.use_datetime > timedelta(
                        minutes = max_disuse_time) \
                        or instance.is_zombie(
                    self.SOLVER_PASS_TIMEOUT_TIMES,
                    self.TRAIN_SOLVERS_TIMEOUT,
                    self.SOLVER_FAILED_ATTEMPTS
                ):
                    instance.stop(self.gateway_stub)
                # En caso contrario añade de nuevo la instancia a su respectiva cola.
                else:
                    self.lock.acquire()
                    solver_config.add_instance(instance, deep = True)
                    self.lock.release()

    def add_service(self, 
            service_with_config: solvers_dataset_pb2.ServiceWithConfig, 
            solver_config_id: str, 
            solver_hash: str,
            stub_class
        ):
        if solver_config_id != SHA3_256(
            value = service_with_config.SerializeToString() # This service not touch metadata, so it can use the hash for id.
        ).hex():
            LOGGER('Solver config not valid ', service_with_config, solver_config_id)
            raise Exception('Solver config not valid ', service_with_config, solver_config_id)

        self.lock.acquire()
        self.solvers.update({
            solver_config_id : ServiceConfig(
                service_with_config = service_with_config,
                service_hash = solver_hash,
                stub_class = stub_class
            )
        })
        self.lock.release()
        try:
            LOGGER('ADDED NEW SOLVER ' + str(solver_config_id) + ' \ndef_ids -> ' +  str(service_with_config.meta.hashtag.hash[0].value.hex()))
        except: LOGGER('ADDED NEW SOLVER ' + str(solver_config_id))

    def get_solver_with_config(self, solver_config_id: str) -> solvers_dataset_pb2.SolverWithConfig:
        return self.solvers[solver_config_id].get_solver_with_config()