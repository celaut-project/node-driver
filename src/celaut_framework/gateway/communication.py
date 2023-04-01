from time import sleep
import os
from typing import List

from grpcbigbuffer.client import Dir, client_grpc
import grpc

from celaut_framework.gateway.protos import gateway_pb2, gateway_pb2_grpc, celaut_pb2
from celaut_framework.gateway.protos.gateway_pb2_grpcbf import StartService_input_partitions, StartService_input, \
    StartService_input_single_partition
from celaut_framework.utils.lambdas import LOGGER


def generate_gateway_stub(gateway_uri: str) -> gateway_pb2_grpc.GatewayStub:
    return gateway_pb2_grpc.GatewayStub(
        grpc.insecure_channel(gateway_uri)
    )


def generate_instance_stub(stub_class, uri: str):
    return stub_class(grpc.insecure_channel(uri))


def __service_extended(
        hashes: List[celaut_pb2.Any.Metadata.HashTag.Hash],
        config: celaut_pb2.Configuration,
        service_hash: str,
        service_directory: str,
        dynamic: bool,
        dev_client: str
):
    use_config: bool = True
    for _hash in hashes:
        if use_config:  # Solo hace falta enviar la configuration en el primer paquete.
            use_config = False
            if dev_client:
                yield gateway_pb2.Client(client_id=dev_client)
            yield gateway_pb2.HashWithConfig(
                hash=_hash,
                config=config,
                min_sysreq=celaut_pb2.Sysresources(
                    mem_limit=80 * pow(10, 6)
                )
            )
        yield _hash

    while not dynamic and os.path.isfile(service_directory + 'services.zip'):
        sleep(1)
        continue

    if os.path.isfile(service_directory + service_hash):
        yield (
            gateway_pb2.ServiceWithMeta,
            Dir(service_directory + service_hash)
        )


def launch_instance(gateway_stub,
                    hashes, config, service_hash,
                    dynamic_service_directory,
                    static_service_directory,
                    dynamic,
                    dev_client,
                    ) -> gateway_pb2.Instance:
    LOGGER('    launching new instance for solver ' + service_hash)
    while True:
        try:
            instance = next(client_grpc(
                method=gateway_stub.StartService,
                input=__service_extended(
                    hashes=hashes,
                    config=config,
                    service_hash=service_hash,
                    service_directory=dynamic_service_directory if dynamic else static_service_directory,
                    dynamic=dynamic,
                    dev_client=dev_client
                ),
                indices_parser=gateway_pb2.Instance,
                partitions_message_mode_parser=True,
                indices_serializer=StartService_input,
                partitions_serializer=StartService_input_partitions if dynamic \
                    else StartService_input_single_partition
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
                method=gateway_stub.StopService,
                input=gateway_pb2.TokenMessage(
                    token=token
                ),
                indices_serializer=gateway_pb2.TokenMessage
            ))
            break
        except grpc.RpcError as e:
            LOGGER('GRPC ERROR STOPPING SOLVER ' + str(e))
            sleep(1)
