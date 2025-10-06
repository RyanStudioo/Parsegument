from typing import Union
from parsegument.CommandGroup import CommandGroup

group = CommandGroup(name="yes")

@group.command
def function(arg1:Union[int,float],arg2:Union[int,float]) -> int:
    return arg1 + arg2

