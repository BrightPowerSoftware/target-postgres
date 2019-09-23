#!/usr/bin/env python

from setuptools import setup, find_packages

def parse_requirements(filename):
    """
    Load requirements from a pip requirements file.
    Taken from bp-config-py:
        https://github.com/BrightPowerSoftware/bp-config-py/blob/40c389d53692d95b877974cf8c74f15469ce0df7/setup.py#L4
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith(("#", "git+ssh"))]


requirements = parse_requirements('requirements.txt')

setup(
    name='singer-target-postgres',
    url='https://github.com/datamill-co/target-postgres',
    author='datamill',
    version="0.2.0",
    description='Singer.io target for loading data into postgres',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    py_modules=['target_postgres'],
    install_requires=requirements,
    setup_requires=[
        "pytest-runner"
    ],
    entry_points='''
      [console_scripts]
      target-postgres=target_postgres:cli
    ''',
    packages=find_packages()
)

