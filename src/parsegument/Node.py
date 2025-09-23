class Node:
    def __init__(self, name) -> None:
        self.name = name

    def execute(self, arguments: list):
        raise NotImplementedError