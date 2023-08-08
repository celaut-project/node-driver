import hashlib
import logging
from typing import Union


def LOGGER(message): logging.getLogger().debug(message + '\n')


# -- The service use sha3-256 for identify internal objects. --
SHA3_256_ID = bytes.fromhex("a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a")


def SHA3_256(value: Union[bytes, bytearray, str]) -> bytes:
    return "" if value is None else hashlib.sha3_256(value).digest()


# Directories

STATIC_SERVICE_DIRECTORY = ''
STATIC_METADATA_DIRECTORY = "__metadata__"
DYNAMIC_SERVICE_DIRECTORY = '__services__'
DYNAMIC_METADATA_DIRECTORY = "__metadata__"
