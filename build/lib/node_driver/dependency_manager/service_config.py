from threading import Lock
from typing import List, Callable, Any, Tuple, Union

from node_driver.dependency_manager.service_instance import ServiceInstance
from node_driver.gateway.communication import generate_instance_stub, launch_instance
from node_driver.gateway.protos import gateway_pb2, celaut_pb2 as celaut
from node_driver.utils.get_grpc_uri import get_grpc_uri, celaut_uri_to_str
from node_driver.utils.lambdas import LOGGER, SHA3_256_ID
from node_driver.utils.network import is_open
from node_driver.utils.read_file import get_from_registry


class ServiceConfig(object):
    def __init__(self,
                 service_hash: str,
                 config: celaut.Configuration,
                 stub_class,
                 timeout: int,
                 failed_attempts: int,
                 pass_timeout_times: int,
                 dynamic: bool,
                 dev_client: str,
                 static_service_directory: str,
                 static_metadata_directory: str,
                 dynamic_service_directory: str,
                 dynamic_metadata_directory: str,
                 check_if_is_alive=None,
                 ):

        self.lock: Lock = Lock()

        self.stub_class = stub_class
        self.dev_client = dev_client
        self.static_service_directory = static_service_directory
        self.static_metadata_directory = static_metadata_directory
        self.dynamic_service_directory = dynamic_service_directory
        self.dynamic_metadata_directory = dynamic_metadata_directory

        self.service_hash: str = service_hash
        self.config: celaut.Configuration = config if config else celaut.Configuration()
        self.hashes = [
            celaut.Any.Metadata.HashTag.Hash(
                type=SHA3_256_ID,
                value=bytes.fromhex(service_hash)
            )
        ]

        # Service's instances.
        self.instances: List[ServiceInstance] = []  # se da uso de una pila para que el 'maintainer' detecte las
        # instancias que quedan en desuso, ya que quedarán estancadas al final de la pila.

        self.check_if_is_alive = check_if_is_alive
        self.timeout = timeout
        self.failed_attempts = failed_attempts
        self.pass_timeout_times = pass_timeout_times

        self.dynamic = dynamic  # Dynamic if is acquired by the api

    def add_instance(self, instance: ServiceInstance, deep=False):
        LOGGER('Add instance ' + str(instance))
        self.instances.append(instance) if not deep else self.instances.insert(0, instance)

    def get_instance(self, deep=False) -> ServiceInstance:
        LOGGER('Get an instance of. deep ' + str(deep))
        LOGGER('The service ' + self.hashes[0].value.hex() + ' has ' + str(len(self.instances)) + ' instances.')
        try:
            return self.instances.pop() if not deep else self.instances.pop(0)
        except IndexError:
            LOGGER('    list empty --> ' + str(self.instances))
            raise IndexError

    def launch_instance(self, gateway_stub) -> ServiceInstance:
        instance = launch_instance(
            gateway_stub=gateway_stub,
            service_hash=self.service_hash,
            hashes=self.hashes,
            config=self.config,
            static_service_directory=self.static_service_directory,
            static_metadata_directory=self.static_metadata_directory,
            dynamic_service_directory=self.dynamic_service_directory,
            dynamic_metadata_directory=self.dynamic_metadata_directory,
            dynamic=self.dynamic,
            dev_client=self.dev_client
        )

        try:
            uri = get_grpc_uri(instance.instance)
        except Exception as e:
            LOGGER(str(e))
            raise e
        LOGGER('The uri for the service ' + self.service_hash + ' is--> ' + str(uri))

        return ServiceInstance(
            stub=generate_instance_stub(
                stub_class=self.stub_class,
                uri=celaut_uri_to_str(uri)
            ),
            token=instance.token,
            check_if_is_alive=self.check_if_is_alive
            if self.check_if_is_alive
            else lambda timeout: is_open(timeout=timeout, ip=uri.ip, port=uri.port)
        )

    def get_service_with_config(self, mem_manager: Callable[[int], Any]) \
            -> Tuple[
                Union[str, celaut.Service],
                Union[str, celaut.Any.Metadata],
                gateway_pb2.Configuration]:
        raise Exception("Not implemented.")

        # return get_from_registry(
        #     service_hash=self.service_hash,
        #     registry=self.dynamic_service_directory if self.dynamic else self.static_service_directory,
        #    mem_manager=mem_manager
        # ), self.config
