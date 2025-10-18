import functools
import inspect
from typing import Optional, Callable
from ..Parameters import Argument, Flag, Operand
from ..error import ParameterNotFound

def _check_if_param_exists(func: Callable, name: str) -> bool:
    signature = inspect.signature(func)
    return name in signature.parameters

def argument(name: str, arg_type: Optional[type]=None) -> Callable:
    """
    Decorator function to modify an argument's information
    """
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, "__parameters__"):
            func.__parameters__ = {"args": {}, "kwargs": {}}
        if not _check_if_param_exists(func, name):
            raise ParameterNotFound(name)
        func.__parameters__["args"][name] = Argument(name, arg_type)
        wrapper.__parameters__ = func.__parameters__

        return wrapper
    return decorator

def flag(name: str) -> Callable:
    """
    Decorator function to modify a flag's information
    """
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, "__parameters__"):
            func.__parameters__ = {"args": {}, "kwargs": {}}
        if not _check_if_param_exists(func, name):
            raise ParameterNotFound(name)
        func.__parameters__["kwargs"][name] = Flag(name)
        wrapper.__parameters__ = func.__parameters__

        return wrapper
    return decorator

def operand(name: str, arg_type: Optional[type]=None) -> Callable:
    """
    Decorator function to modify an operand's information
    """
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, "__parameters__"):
            func.__parameters__ = {"args": {}, "kwargs": {}}
        if not _check_if_param_exists(func, name):
            raise ParameterNotFound(name)
        func.__parameters__["kwargs"][name] = Operand(name, arg_type)
        wrapper.__parameters__ = func.__parameters__
        return wrapper
    return decorator