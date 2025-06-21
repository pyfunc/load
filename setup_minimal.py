#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Minimal setup.py for Python 2.7 compatibility testing.
"""
from __future__ import print_function, unicode_literals

import os
import sys
from setuptools import setup, find_packages

# Get the package version
about = {}
with open(os.path.join('src', 'load', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, about)
            break

setup(
    name='load',
    version=about.get('__version__', '1.0.0'),
    description='Modern Python import alternative with automatic package installation',
    author='Tom Sapletta',
    author_email='info@softreck.dev',
    url='https://github.com/pyfunc/load',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'six>=1.16.0',
        'future>=1.0.0',
        'pathlib2>=2.3.0;python_version<"3.0"',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
)
