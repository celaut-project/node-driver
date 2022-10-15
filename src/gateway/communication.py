from time import sleep
from typing import Tuple

from grpcbigbuffer import Dir, client_grpc
from gateway_pb2_grpcbf import StartService_input_partitions, StartService_input
import grpc

from gateway.protos import gateway_pb2_grpcbf, gateway_pb2
from protos import celaut_pb2
from utils.lambdas import LOGGER


def generate_gateway_stub(gateway_uri: str) -> gateway_pb2_grpc.GatewayStub:
    return gateway_pb2_grpc.GatewayStub(grpc.insecure_channel(gateway_uri))


def generate_instance_stub(stub_class, uri):
    return stub_class(grpc.insecure_channel(uri))


def modify_resources_grpcbb(i: dict) -> Tuple[api_pb2.celaut__pb2.Sysresources, int]:
    output: gateway_pb2_grpcbf.ModifyServiceSystemResourcesOutput = next(
        client_grpc(
            method = gateway_pb2_grpc.GatewayStub(
                        grpc.insecure_channel(ENVS['GATEWAY_MAIN_DIR'])
                    ).ModifyServiceSystemResources,
            input = gateway_pb2_grpcbf.ModifyServiceSystemResourcesInput(
                min_sysreq = celaut_pb2.Sysresources(
                    mem_limit = i['min']
                ),
                max_sysreq = celaut_pb2.Sysresources(
                    mem_limit = i['max']
                ),
            ),
            partitions_message_mode_parser=True,
            indices_parser = gateway_pb2_grpcbf.ModifyServiceSystemResourcesOutput,
        )
    )
    return output.sysreq, to_gas_amount(output.gas)

def service_extended(hashes, config, solver_hash, dynamic_service_instances):
    use_config = True
    for hash in hashes:
        if use_config:  # Solo hace falta enviar la configuracion en el primer paquete.
            use_config = False
            yield gateway_pb2_grpcbf.HashWithConfig(
                hash = hash,
                config = config
            )
        yield hash
    yield (
        gateway_pb2_grpcbf.ServiceWithMeta,
        Dir(dynamic_service_instances + solver_hash+'/p1'),
        Dir(dynamic_service_instances + solver_hash+'/p2')
    )


def service_extended_from_disk(hashes, config, static_service_directory):
    use_config = True
    for hash in hashes:
        if use_config:  # Solo hace falta enviar la configuracion en el primer paquete.
            use_config = False
            yield gateway_pb2_grpcbf.HashWithConfig(
                hash = hash,
                config = config,
                min_sysreq = gateway_pb2_grpcbf.celaut__pb2.Sysresources(
                    mem_limit = 80*pow(10, 6)
                )
            )
        yield hash
    while True:
        if not os.path.isfile(static_service_directory + 'services.zip'):
            yield gateway_pb2.ServiceWithMeta, Dir(static_service_directory + 'regresion.service')
            break
        else:
            sleep(1)
            continue

def launch_instance(self, gateway_stub,
                        hashes, config, solver_hash,
                        dynamic_service_instances, static_service_instances
                    ) -> gateway_pb2_grpcbf.Instance:
    LOGGER('    launching new instance for solver ' + self.solver_hash)
    while True:
        try:
            instance = next(client_grpc(
                method=gateway_stub.StartService,
                input=service_extended(hashes, config, solver_hash, dynamic_service_instances),
                indices_parser=gateway_pb2_grpcbf.Instance,
                partitions_message_mode_parser=True,
                indices_serializer=StartService_input,
                partitions_serializer=StartService_input_partitions
            ))
            break
        except grpc.RpcError as e:
            LOGGER('GRPC ERROR LAUNCHING INSTANCE. ' + str(e))
            sleep(1)

    return instance

def stop(gateway_stub, token: str):
    LOGGER('Stops this instance with token ' + str(token))
    while True:
        try:
            next(client_grpc(
                method = gateway_stub.StopService,
                input = gateway_pb2_grpcbf.TokenMessage(
                            token = token
                        ),
                indices_serializer = gateway_pb2_grpcbf.TokenMessage
            ))
            break
        except grpc.RpcError as e:
            LOGGER('GRPC ERROR STOPPING SOLVER ' + str(e))
            sleep(1)


def to_gas_amount(gas_amount: int) -> gateway_pb2_grpcbf.GasAmount:
    return gateway_pb2_grpcbf.GasAmount(n = str(gas_amount))

def from_gas_amount(gas_amount: gateway_pb2_grpcbf.GasAmount) -> int:
    return int(gas_amount.n)