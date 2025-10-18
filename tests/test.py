import parsegument as pg

parser = pg.Parsegumenter()

@parser.command()
@pg.argument("bar", float)
def foo(bar:int, bar2:bool=False):
    print(bar + 10)
    print(type(bar))
    print(bar2)

print(parser.execute("foo 10.9 -bar2"))