from setuptools import setup, find_packages

setup(
    name='celautframework',
    version='__dev__',

    url='https://github.com/jossemii/CelautFramework.git',
    author='Josemi Avellana',
    author_email='josemi.bnf@gmail.com',

    py_modules=['celaut_framework'],
    install_requires=[
        'grpcio==1.48.1',
        'protobuf==3.19.4',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)