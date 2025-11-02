from typing import Callable
from string import Template

class HelpFormatter:
    triggers = ["-help", "--help", "-h"]

    def __init__(self,
                 schema: str =
                 """
                 Usage: {usage}
                 
                 {description}
                 
                 [Options]
                 {options}
                 """
                 ):
        self.schema = schema

    @classmethod
    def is_help_message(cls, nodes: list[str]):
        return bool([i for i in nodes if i in cls.triggers])

    @classmethod
    def first_node_is_help(cls, nodes: list[str]):
        return nodes[0] in cls.triggers

    def create_message(self, usage: str, description: str, options: str):
        return self.schema.format(usage=usage, description=description, options=options)