#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the load package.
Compatible with Python 2.7 and 3.5+.
"""
from __future__ import print_function, unicode_literals

import io
import os
import sys
from setuptools import setup, find_packages

# Handle Python 2/3 compatibility
PY2 = sys.version_info[0] == 2

# Read the README file for the long description
here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the package version
about = {}
with io.open(os.path.join(here, 'src', 'load', '__init__.py'), encoding='utf-8') as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, about)
            break

# Dependencies
install_requires = [
    'six>=1.16.0,<2.0.0',
    'future>=1.0.0,<2.0.0',
]

# Add pathlib2 for Python 2.7
if PY2:
    install_requires.append('pathlib2>=2.3.0')

setup(
    name='load',
    version=about.get('__version__', '1.0.0'),
    description='Modern Python import alternative with automatic package installation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about.get('__author__', 'Tom Sapletta'),
    author_email=about.get('__email__', 'info@softreck.dev'),
    url='https://github.com/pyfunc/load',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'load-info=load.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='import package management automatic installation',
    project_urls={
        'Documentation': 'https://github.com/pyfunc/load#readme',
        'Source': 'https://github.com/pyfunc/load',
        'Tracker': 'https://github.com/pyfunc/load/issues',
    },
)
