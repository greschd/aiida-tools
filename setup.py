#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    20.10.2014 11:27:40 CEST
# File:    setup.py

import re
from setuptools import setup

readme = """Helper tools for AiiDA."""

with open('./aiida_tools/_version.py', 'r') as f:
    match_expr = "__version__[^'" + '"]+([' + "'" + r'"])([^\1]+)\1'
    version = re.search(match_expr, f.read()).group(2)

setup(
    name='aiida-tools',
    version=version,
    url='http://z2pack.ethz.ch/aiida-tools',
    author='Dominik Gresch',
    author_email='greschd@gmx.ch',
    description=readme,
    install_requires=['decorator'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Development Status :: 3 - Alpha'
    ],
    license='GPL',
    packages=['aiida_tools']
)
