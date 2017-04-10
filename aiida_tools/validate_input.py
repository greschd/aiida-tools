#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

"""
Decorators to simplify validating the input of workflows.
"""

from __future__ import division, print_function, unicode_literals

import types
from collections import namedtuple

from aiida.common.exceptions import InputValidationError

from decorator import decorator

class _Parameter(object):
    def __init__(self, type, required):
        self.type = type
        self.required = bool(required)

def _init_params(cls):
    if not hasattr(cls, '_params'):
        cls._params = dict()

def parameter(name, type=None, required=True):
    def inner(cls):
        _init_params(cls)
        cls._params[name] = _Parameter(type=type, required=required)
        return cls
    return inner

def inherit_parameters(workflow, ignore=()):
    def inner(cls):
        _init_params(cls)
        inherited = getattr(workflow, '_params', dict())
        cls._params.update(
            {key: val for key, val in inherited.items() if key not in ignore}
        )
        return cls
    return inner

def validate_input(cls):
    @decorator
    def _run_validate(func, self, *args, **kwargs):
        params = self.get_parameters()
        valid_params = getattr(cls, '_params', dict())

        for name, val in valid_params.items():
            try:
                r = params.pop(name)
            except KeyError:
                if val.required:
                    raise InputValidationError("Missing required parameter '{}'.".format(name))
                else:
                    continue
            if not isinstance(r, val.type):
                raise InputValidationError("Input parameter '{}' is of invalid type '{}'; should be '{}'.".format(name, type(r), val.type))
        self.append_to_report('Input validation passed. Starting workflow with the following parameters:' + ''.join(
            ['\n    {}: {}'.format(key, val) for key, val in sorted(self.get_parameters().items())]
        ))
        return func(self, *args, **kwargs)
    cls.start = _run_validate(cls.start.__func__)
    return cls
