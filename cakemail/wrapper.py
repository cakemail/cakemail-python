from functools import wraps

from cakemail.response import Response


def wrapper(method):
    @wraps(method)
    def wrapped(*args, **kwargs):
        obj = method(*args, **kwargs)
        return Response(obj)

    return wrapped


class WrappedApi:
    def __init__(self, superclass, suffix):
        for name in dir(superclass):
            if name.endswith(f'_{suffix}'):
                """ singular """
                short = name.split(f'_{suffix}')[0]
                setattr(self, short, wrapper(getattr(superclass, name)))
            elif name.endswith(f'_{suffix}s'):
                """ plural """
                short = name.split(f'_{suffix}s')[0]
                setattr(self, short, wrapper(getattr(superclass, name)))
