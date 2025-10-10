import inspect
import typing

from parsegument import CommandGroup

@CommandGroup("yes").command
def foo(bar: typing.OrderedDict, test: int=1, test2: typing.Union[int, float]=2):
    print(type(bar))
