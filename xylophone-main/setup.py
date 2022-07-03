#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='xylophone',
    version='1.0.0',
    license='MIT',
    packages=find_packages(
        where='.',
        include=['xylophone*'],
    ),
)

