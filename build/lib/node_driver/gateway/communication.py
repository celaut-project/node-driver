from time import sleep
import os
from typing import List, Tuple

from grpcbigbuffer.client import Dir, client_grpc
import grpc

from node_driver.gateway.protos import gateway_pb2, gateway_pb2_grpc, celaut_pb2
from node_driver.gateway.protos.gateway_pb2_grpcbf import StartService_input_indices
from node_driver.gateway.utils import from_gas_amount
from node_driver.utils.lambdas import LOGGER


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
        metadata_directory: str,
        dynamic: bool,
        dev_client: str
):
    if dev_client:
        yield gateway_pb2.Client(client_id=dev_client)

    yield gateway_pb2.Configuration(
                config=config,
                resources=gateway_pb2.CombinationResources(clause={
                    1: gateway_pb2.CombinationResources.Clause(
                        min_sysreq=celaut_pb2.Sysresources(
                            mem_limit=80 * pow(10, 6)
                        )
                    )
                })
            )

    for _hash in hashes:
        yield _hash

    # TODO could use async here.
    while not dynamic and os.path.isfile(os.path.join(service_directory, 'services.zip')):
        sleep(1)
        continue

    if os.path.exists(os.path.join(metadata_directory, service_hash)):
        yield Dir(dir=os.path.join(metadata_directory, service_hash), _type=celaut_pb2.Any.Metadata)

    if os.path.exists(os.path.join(service_directory, service_hash)):
        yield Dir(dir=os.path.join(service_directory, service_hash), _type=celaut_pb2.Service)


def launch_instance(gateway_stub,
                    hashes, config, service_hash,
                    static_service_directory: str,
                    static_metadata_directory: str,
                    dynamic_service_directory: str,
                    dynamic_metadata_directory: str,
                    dynamic: bool,
                    dev_client,
                    ) -> gateway_pb2.Instance:
    LOGGER('    launching new instance for service ' + service_hash)
    while True:
        try:
            instance: gateway_pb2.Instance = next(client_grpc(
                method=gateway_stub.StartService,
                input=__service_extended(
                    hashes=hashes,
                    config=config,
                    service_hash=service_hash,
                    service_directory=dynamic_service_directory if dynamic else static_service_directory,
                    metadata_directory=dynamic_metadata_directory if dynamic else static_metadata_directory,
                    dynamic=dynamic,
                    dev_client=dev_client
                ),
                indices_parser=gateway_pb2.Instance,
                partitions_message_mode_parser=True,
                indices_serializer=StartService_input_indices,
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


def modify_resources(i: dict, gateway_main_dir: str) -> Tuple[celaut_pb2.Sysresources, int]:
    output: gateway_pb2.ModifyServiceSystemResourcesOutput = next(
        client_grpc(
            method=gateway_pb2_grpc.GatewayStub(
                grpc.insecure_channel(gateway_main_dir)
            ).ModifyServiceSystemResources,
            input=gateway_pb2.ModifyServiceSystemResourcesInput(
                min_sysreq=celaut_pb2.Sysresources(
                    mem_limit=i['min']
                ),
                max_sysreq=celaut_pb2.Sysresources(
                    mem_limit=i['max']
                ),
            ),
            partitions_message_mode_parser=True,
            indices_parser=gateway_pb2.ModifyServiceSystemResourcesOutput,
        )
    )
    return output.sysreq, from_gas_amount(output.gas)
