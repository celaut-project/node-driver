def generator(filename):
    with open(filename, 'rb') as entry:
        for chunk in iter(lambda: entry.read(1024 * 1024), b''):
            yield chunk

def read_file(filename) -> bytes:
    return b''.join([b for b in generator(filename)])