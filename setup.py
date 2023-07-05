from setuptools import setup, find_packages

setup(
    name='node_driver',
    version='0.0.1',

    url='https://github.com/jossemii/CelautFramework.git',
    author='J.Avellana',
    author_email='jossemii@proton.me',

    py_modules=['node_driver'],
    install_requires=[
        'grpcbigbuffer@git+https://github.com/jossemii/GRPCBigBuffer',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
)