

class HelpMessageFormatter:
    triggers = ["-help", "--help", "-h"]
    def __init__(self):
        pass

    @classmethod
    def is_help_message(cls, nodes: list[str]):
        return bool([i for i in nodes if i in cls.triggers])

    @classmethod
    def first_node_is_help(cls, nodes: list[str]):
        return nodes[0] in cls.triggers