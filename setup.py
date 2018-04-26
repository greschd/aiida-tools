#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    20.10.2014 11:27:40 CEST
# File:    setup.py

import re
from setuptools import setup

readme = """Helper tools for AiiDA."""

# Get the version number
with open('./aiida_tools/__init__.py') as f:
    match_expr = "__version__[^'\"]+(['\"])([^'\"]+)"
    version = re.search(match_expr, f.read()).group(2).strip()


setup(
    name='aiida-tools',
    version=version,
    url='http://z2pack.ethz.ch/aiida-tools',
    author='Dominik Gresch',
    author_email='greschd@gmx.ch',
    description=readme,
    install_requires=['fsc.export', 'pyyaml'],
    extras_require={
        ':python_version < "3"': ['singledispatch'],
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Framework :: AiiDA',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Development Status :: 3 - Alpha'
    ],
    license='GPL',
    packages=['aiida_tools']
)
