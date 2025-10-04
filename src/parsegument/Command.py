from typing import Callable, Union
from .Node import Node
from .Arguments import Argument, Operand, Flag
<<<<<<< HEAD
import inspect
from .utils.parser import node_type, parse_operand
=======
>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017

class Command(Node):
    def __init__(self, name: str, executable: Callable) -> None:
        super().__init__(name)
        self.arguments = {
            "args": [],
            "kwargs": {}
                          }
<<<<<<< HEAD
        self.executable = executable
=======
>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017

    def add_node(self, arg: Union[Argument, Operand, Flag]) -> None:
        if isinstance(arg, Argument):
            self.arguments["args"].append(arg)
        elif isinstance(arg, Operand):
            self.arguments["kwargs"].append(arg)
        elif isinstance(arg, Flag):
            self.arguments["kwargs"].append(arg)

    def execute(self, nodes:list[str]):
<<<<<<< HEAD
        args_length = len(self.arguments["args"])
        args = nodes[:args_length+1]
        kwargs_strings = nodes[args_length+1:]
        kwargs = {}
        for kwarg_string in kwargs_strings:
            type_node = node_type(kwarg_string)
            if type_node == "Flag":
                kwargs[kwarg_string] = True
                continue
            else:
                value = parse_operand(kwarg_string)
                kwargs[kwarg_string] = value
                continue
        self.executable(*args, **kwargs)
=======
        for node in nodes:
            pass

>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017
