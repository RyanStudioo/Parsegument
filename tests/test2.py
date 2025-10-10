import inspect
import typing

from parsegument import CommandGroup

def foo(bar: typing.OrderedDict, test: int=1):
    print(type(bar))

signature = inspect.signature(foo)
print(signature.parameters)
for key, param in signature.parameters.items():
    print(param.annotation)