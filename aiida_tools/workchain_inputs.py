try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch

from fsc.export import export
import plum.util

from aiida.orm.data.base import Str

__all__ = ['WORKCHAIN_INPUT_KWARGS']

@export
@singledispatch
def get_fullname(cls_obj):
    return Str(plum.util.fullname(cls_obj))


@get_fullname.register(str)
def _(cls_name):
    return Str(cls_name)


@get_fullname.register(Str)
def _(cls_name):
    return cls_name

@export
def load_class(cls_name):
    return plum.util.load_class(cls_name.value)


WORKCHAIN_INPUT_KWARGS = {
    'valid_type': Str,
    'serialize_fct': get_fullname,
    'deserialize_fct': load_class
}
