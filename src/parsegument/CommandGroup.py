import typing
from typing import Union, Callable, get_origin
from inspect import signature
from .Node import Node
from .Command import Command
from .error import NodeDoesNotExist
from .utils.convert_params import convert_param

class CommandGroup(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children = {}

    def add_child(self, node:Union[Command, "CommandGroup"]) -> None:
        self.children[node.name] = node

    def command(self, func: Callable):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        params = signature(func).parameters
        func_name = func.__name__
        command_object = Command(name=func_name, executable=func)
        for key, param in params.items():
            converted = convert_param(param)
            command_object.add_node(converted)
        self.add_child(command_object)
        print(command_object)
        return wrapper

    def execute(self, nodes:list[str]):
        child = self.children.get(nodes[0])
        if not child:
            raise NodeDoesNotExist
        return child.execute(nodes[1:])
