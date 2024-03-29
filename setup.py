from setuptools import setup, find_packages

setup(
    name='node_driver',
    version='0.0.1',

    url='https://github.com/celaut-project/node-driver.git',
    author='jossemii',
    author_email='jossemii@proton.me',

    py_modules=['node_driver'],
    install_requires=[
        'pee-rpc@git+https://github.com/pee-rpc-protocol/pee-rpc',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
)
