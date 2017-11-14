import functools

from fsc.export import export


@export
def check_workchain_step(func):
    """
    Decorator for workchain steps that logs (and re-raises) errors occuring within that step.
    """
    @functools.wraps(func)
    def inner(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            self.report(
                '{} in {}: {}'.format(type(e).__name__, func.__name__, e)
            )
            raise e

    return inner
