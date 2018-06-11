"""
Contains default keyword arguments to pass classes as input to workchains.
"""

try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch

import yaml
from fsc.export import export
from aiida.work.class_loader import CLASS_LOADER

from aiida.orm.data.base import Str

__all__ = ['WORKCHAIN_INPUT_KWARGS']

@export
@singledispatch
def get_fullname(cls_obj):
    """
    Serializes an AiiDA workchain or workfunction to an AiiDA String. For workchains the class identifier is used, workfunctions are serialized in YAML format.

    :param cls_obj: Object to be serialized
    :type cls_obj: WorkChain, workfunction
    """
    try:
        return Str(CLASS_LOADER.class_identifier(cls_obj))
    except ValueError:
        return Str(yaml.dump(cls_obj))


@get_fullname.register(str)
def _(cls_name):
    return Str(cls_name)

#: Keyword arguments to be passed to ``spec.input`` for serializing an input which is a class / workchain into a string.
WORKCHAIN_INPUT_KWARGS = {
    'valid_type': Str,
    'serializer': get_fullname,
}

@export
def load_object(cls_name):
    """
    Loads the workchain or workfunction from the serialized string.
    """
    cls_name_str = cls_name.value
    try:
        return CLASS_LOADER.load_class(cls_name_str)
    except ValueError:
        return yaml.load(cls_name_str)
