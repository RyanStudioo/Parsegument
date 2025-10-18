import functools
import inspect

from ..Parameters import Argument, Flag, Operand
from ..error import ParameterNotFound, CommandNotFound

def check_if_param_exists(func, name):
    signature = inspect.signature(func)
    return name in signature.parameters

def argument(name: str, arg_type: type):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, "__parameters__"):
            func.__parameters__ = {"args": {}, "kwarg": {}}
        if not check_if_param_exists(func, name):
            raise ParameterNotFound(name)
        func.__parameters__["args"][name] = Argument(name, arg_type)
        wrapper.__parameters__ = func.__parameters__

        return wrapper
    return decorator