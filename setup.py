#!/usr/bin/env python3

from setuptools import setup

setup(
    name='mqtt-driver',
    version='0.0.1',
    packages=['mqtt-driver'],
    scripts=['bin/mqtt-driver.py'],
    install_requires=[
        'paho-mqtt',
        'requests',
        'redis'
    ]
)   

