from aiida.common.exceptions import InputValidationError

__all__ = ['get_input_validator']

def get_input_validator(inputdict):
    def _validate_input(name, valid_types, required=True, default=None):
        try:
            value = inputdict.pop(name)
        except KeyError:
            if required:
                raise InputValidationError("Missing required input parameter '{}'".format(name))
            else:
                value = default

        if not isinstance(valid_types, (list, tuple)):
            valid_types = [valid_types]
        if not required:
            valid_types = list(valid_types) + [type(default)]
        valid_types = tuple(valid_types)

        if not isinstance(value, valid_types):
            raise InputValidationError("Input parameter '{}' is of type '{}', but should be of type(s) '{}'".format(name, type(value), valid_types))
        return value

    return _validate_input
