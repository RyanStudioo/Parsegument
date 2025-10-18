from typing import Callable, Union, Any
from .Parameters import Argument, Operand, Flag
import inspect

from .types.ArgDict import ArgDict
from .utils.parser import node_type, parse_operand, convert_string_to_result

class Command:
    """
    Linked to a function via executable
    """
    parameters: ArgDict

    def __init__(self, name: str, executable: Callable) -> None:
        self.name = name
        self.parameters = {"args": {}, "kwargs": {}}
        self.executable = executable

    def add_parameter(self, arg: Union[Argument, Operand, Flag]) -> None:
        """defines an argument, operand, or flag to the command"""
        if type(arg) == Argument:
            self.parameters["args"][arg.name] = arg
        else:
            self.parameters["kwargs"][arg.name] = arg

    def execute(self, nodes:list[str]) -> Any:
        """Converts all arguments in nodes into its defined types, and executes the linked executable"""
        args_length = len(self.parameters["args"])
        args = nodes[:args_length]
        args = {name:args[idx] for idx, name in enumerate(self.parameters["args"].keys())}
        args = [convert_string_to_result(value, self.parameters["args"][key].arg_type) for key, value in args.items()]
        kwargs_strings = nodes[args_length:]
        kwargs = {}
        for kwarg_string in kwargs_strings:
            type_of_node = node_type(kwarg_string)
            if type_of_node == "Flag":
                kwargs[kwarg_string[1:]] = True
                continue
            elif type_of_node == "Operand":
                name, value = parse_operand(kwarg_string)
                node_arguments = self.parameters["kwargs"][name]
                value = convert_string_to_result(value, node_arguments.arg_type)
                kwargs[name] = value
                continue
        return self.executable(*args, **kwargs)
