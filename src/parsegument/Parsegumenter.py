from __future__ import annotations
from typing import Union
from .error import NodeDoesNotExist, ArgumentGroupNotFound, MultipleChildrenFound
import shlex

if annotations:
    from .Arguments import Argument
    from .CommandGroup import CommandGroup
    from .Command import Command


class Parsegumenter:
    def __init__(self) -> None:
        self.children = {}


    def add_child(self, child: Union[CommandGroup, Command]):
        if child.name in [i.name for i in self.children]:
            return False
        self.children[child.name] = child
        return True

    def execute(self, command:Union[str, list[str]]):
        parsed = shlex.split(command) if isinstance(command, str) else command
        child_name = parsed[0]
        arguments = parsed[1:]
        child_command = self.children.get(child_name)
        if not child_command:
            raise NodeDoesNotExist
        return child_command.execute(arguments)

