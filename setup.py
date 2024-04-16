from setuptools import setup, find_packages

# Project metadata
NAME = 'Assignment02 - DOT503'
VERSION = '1.0.0'
DESCRIPTION = 'Simple Calculator Application'
AUTHOR = 'Vimantha Perera'
EMAIL = 'vimanthaperera9@gmail.com'
URL = 'https://github.com/VimanthaPerera09/calculator.git'
LICENSE = 'MIT'

# Dependencies
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    install_requires=required_packages,
    entry_points={
        'console_scripts': [
            'my_project = calc:main',  # Replace 'calculator' with your main module
        ],
    },
)
