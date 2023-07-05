import os

from grpcbigbuffer.utils import WITHOUT_BLOCK_POINTERS_FILE_NAME

from celaut_driver.gateway.protos import gateway_pb2
from celaut_driver.resource_manager.resourcemanager import mem_manager


def generator(filename):
    with open(filename, 'rb') as entry:
        for chunk in iter(lambda: entry.read(1024 * 1024), b''):
            yield chunk


def read_file(filename) -> bytes:
    return b''.join([b for b in generator(filename)])


def get_from_registry(service_hash: str, registry: str) -> gateway_pb2.ServiceWithMeta():
    filename: str = registry + service_hash
    if not os.path.exists(filename):
        raise Exception("Error reading the file. It doesn't exists.")

    if os.path.isdir(filename):
        filename = filename + '/' + WITHOUT_BLOCK_POINTERS_FILE_NAME
    try:
        with mem_manager(2 * os.path.getsize(filename)):
            service = gateway_pb2.ServiceWithMeta()
            service.ParseFromString(read_file(filename=filename))
            return service
    except (IOError, FileNotFoundError):
        raise Exception("Error reading the file.")