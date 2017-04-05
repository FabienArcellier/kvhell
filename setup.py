#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='kvhell',
    version='0.0.1',
    packages=find_packages(exclude=["*_tests"]),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires = {
      'tornado',
      'pytest',
      'pytest-benchmark',
      'requests',
      'Faker'
    }
)
