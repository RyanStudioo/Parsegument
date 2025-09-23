from typing import Callable, Union
from .Node import Node
from .Arguments import Argument, Operand, Flag

class Command(Node):
    def __init__(self, name: str, executable: Callable) -> None:
        super().__init__(name)
        self.arguments = {
            "args": [],
            "kwargs": {}
                          }

    def add_node(self, arg: Union[Argument, Operand, Flag]) -> None:
        if isinstance(arg, Argument):
            self.arguments["args"].append(arg)
        elif isinstance(arg, Operand):
            self.arguments["kwargs"].append(arg)
        elif isinstance(arg, Flag):
            self.arguments["kwargs"].append(arg)

    def execute(self, nodes:list[str]):
        for node in nodes:
            pass

