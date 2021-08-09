from setuptools import find_packages
from setuptools import setup

setup(
    name='pollo',
    version='0.0.1',
    description='Proyecto del pollo mas poderoso',
    author='ChepeCarlos',
    author_email='chepecarlos@alswblog.org',
    url='https://github.com/chepecarlos/ElPollo',
    install_requires=[],
    packages=find_packages(exclude=('tests*','testing*')),
    entry_points={
        'console_scripts': [
            'pollo-cli = pollo.main:main'
        ]
    },
)