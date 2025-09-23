from .Node import Node

class Argument(Node):
    def __init__(self, name: str, arg_type:type=str) -> None:
        super().__init__(name)
        self.arg_type = arg_type

class Flag(Node):
    def __init__(self, name):
        super().__init__(name)

class Operand(Node):
    def __init__(self, name: str, arg_type:type=str) -> None:
        super().__init__(name)
        self.arg_type = arg_type

