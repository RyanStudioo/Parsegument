from typing import Dict
import parsegument as pg

parser = pg.Parsegumenter()

@parser.command()
@pg.argument("bar", float)
@pg.operand("bar2", bool)
def foo(bar:int, bar2:Dict=1.1):
    print(bar + 10)
    print(type(bar))
    print(bar2)

print(parser.execute("foo 10.9 --bar2=1.3"))