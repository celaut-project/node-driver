from time import sleep
import os

from grpcbigbuffer import Dir, client_grpc
from gateway_pb2_grpcbf import StartService_input_partitions, StartService_input
import grpc

from gateway.protos import gateway_pb2, gateway_pb2_grpc
from protos import celaut_pb2
from utils.lambdas import LOGGER


def generate_gateway_stub(gateway_uri: str) -> gateway_pb2_grpc.GatewayStub:
    return gateway_pb2_grpc.GatewayStub(grpc.insecure_channel(gateway_uri))


def generate_instance_stub(stub_class, uri):
    return stub_class(grpc.insecure_channel(uri))


def service_extended(hashes, config, solver_hash, dynamic_service_instances, dev_client):
    use_config = True
    for hash in hashes:
        if use_config:  # Solo hace falta enviar la configuracion en el primer paquete.
            use_config = False
            if dev_client: yield gateway_pb2.Client(client_id = dev_client)
            yield gateway_pb2.HashWithConfig(
                hash = hash,
                config = config,
                min_sysreq=celaut_pb2.Sysresources(
                    mem_limit=80 * pow(10, 6)
                )
            )
        yield hash
    yield (
        gateway_pb2.ServiceWithMeta,
        Dir(dynamic_service_instances + solver_hash+'/p1'),
        Dir(dynamic_service_instances + solver_hash+'/p2')
    )


def service_extended_from_disk(hashes, config, static_service_directory, dev_client):
    use_config = True
    for hash in hashes:
        if use_config:  # Solo hace falta enviar la configuracion en el primer paquete.
            use_config = False
            if dev_client: yield gateway_pb2.Client(client_id=dev_client)
            yield gateway_pb2.HashWithConfig(
                hash = hash,
                config = config,
                min_sysreq = celaut_pb2.Sysresources(
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
                    hashes, config, service_hash,
                    dynamic_service_directory, static_service_directory
                    ) -> gateway_pb2.Instance:
    LOGGER('    launching new instance for solver ' + self.service_hash)
    while True:
        try:
            instance = next(client_grpc(
                method=gateway_stub.StartService,
                input=service_extended(hashes, config, service_hash, dynamic_service_directory),
                indices_parser=gateway_pb2.Instance,
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
                input = gateway_pb2.TokenMessage(
                            token = token
                        ),
                indices_serializer = gateway_pb2.TokenMessage
            ))
            break
        except grpc.RpcError as e:
            LOGGER('GRPC ERROR STOPPING SOLVER ' + str(e))
            sleep(1)