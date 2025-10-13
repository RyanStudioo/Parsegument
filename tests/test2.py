import parsegument
from parsegument import CommandGroup

parser = parsegument.Parsegumenter()

@parser.command
def foo(bar: str, test: int=1, test2: float=2.0):
    print(bar, test, test2)
    print(type(bar), type(test), type(test2))

parser.execute("foo testing --test=5 --test2=10.3")