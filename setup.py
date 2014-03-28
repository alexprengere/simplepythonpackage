#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'Aggregation',
    version = '0.1',
    author = 'Alex Prengère',
    author_email = 'alexprengere@gmail.com',
    url = 'https://github.com/alexprengere/simplepythonpackage',
    description = 'A minimalist Python package, with packaging, docs and tests.',
    long_description = open('README.rst'),
    license = open('LICENSE'),
    py_modules = ['aggregation'],
    data_files = [
        ('data', ['data/flights.csv'])
    ]
)
