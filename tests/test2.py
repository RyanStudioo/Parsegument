from typing import Optional, Any

import parsegument as pg
from parsegument import CommandGroup

class ChildGroup(CommandGroup):
    def __init__(self):
        super().__init__("ChildGroup")

    @staticmethod
    @pg.argument("test", int)
    def method_thing(test:str) -> Optional[Any]:
        if type(test) == str:
            return test + ", This is a method thing"
        elif type(test) == int:
            return test + 2
        return None


parser = pg.Parsegumenter()
group = ChildGroup()
group.initialise()
parser.add_child(group)
print(parser.execute("ChildGroup method_thing 10.5"))
print(parser.schema)