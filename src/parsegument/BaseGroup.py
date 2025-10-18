from __future__ import annotations
from typing import Union, Callable, TYPE_CHECKING
from inspect import signature
import functools
from .utils.convert_params import convert_param
from .Command import Command
from .Node import Node

if TYPE_CHECKING:
    from .CommandGroup import CommandGroup


class BaseGroup(Node):
    def __init__(self, name:str, help=""):
        super().__init__(name, help)
        self.children = {}

    @classmethod
    def _get_methods(cls) -> set[str]:
        return set([i for i in dir(cls) if i[0] != "_"])

    def add_child(self, child: Union[Command, CommandGroup]) -> bool:
        """Add a Command or CommandGroup as a child"""
        if child.name in [i.name for i in self.children]:
            return False
        self.children[child.name] = child
        return True

    def command(self, name:str=None) -> Callable:
        """A Decorator that automatically creates a command, and adds it as a child"""

        def command_wrapper(func):
            orig = getattr(func, "__wrapped__", func)
            params = signature(func).parameters
            func_name = func.__name__
            command_object = Command(name=func_name, executable=func)
            for key, param in params.items():
                converted = convert_param(param)
                command_object.add_parameter(converted)
            if name:
                command_object.name = name
            self.add_child(command_object)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            new_params = getattr(func, "__parameters__", None) or getattr(orig, "__parameters__", None)
            if new_params:
                for arg in new_params["args"].values():
                    command_object.parameters["args"][arg.name] = arg
                for kwarg in new_params["kwargs"].values():
                    command_object.parameters["kwargs"][kwarg.name] = kwarg
            wrapper.command = command_object
            orig.command = command_object


            return wrapper

        return command_wrapper

    def execute(self, nodes: Union[str, list[str]]):
        raise NotImplementedError

