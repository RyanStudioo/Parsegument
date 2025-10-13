import parsegument as pg
from parsegument import CommandGroup

class ChildGroup(CommandGroup):
    def __init__(self):
        super().__init__("ChildGroup")

    def method_thing(self, test:str):
        """Documentation"""
        print(test)
        pass

print(ChildGroup.method_thing.__doc__)