import parsegument as pg

parser = pg.Parsegumenter()

@parser.command(name="foo2")
def foo(bar:int):
    print(bar + 10)

parser.run()