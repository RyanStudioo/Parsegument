from .Node import Node

class Argument(Node):
    """A Compulsory Argument"""
    def __init__(self, name: str, arg_type:type=str) -> None:
        super().__init__(name)
        self.arg_type = arg_type

class Flag(Argument):
    """An optional boolean kwarg"""
    def __init__(self, name:str) -> None:
        super().__init__(name, bool)

class Operand(Argument):
    """Any keyword Argument"""
    def __init__(self, name: str, arg_type:type=str) -> None:
        super().__init__(name, arg_type)

