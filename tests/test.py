import parsegument as pg

parser = pg.Parsegumenter()

@parser.command()
@pg.argument("bar", float)
def foo(bar:int):
    print(bar + 10)
    print(type(bar))

print(parser.execute("foo 10.9"))