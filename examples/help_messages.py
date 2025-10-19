import parsegument as pg

parser = pg.Parsegumenter(name="Parsegument", help="Base Command Group")
group = pg.CommandGroup(name="group", help="another group")
parser.add_child(group)

@group.command(name="foo", help="prints the argument")
@pg.argument("bar", help="string to print out")
def foo(bar: str):
    print(bar)

@group.command(name="foo2", help="prints the argument again")
@pg.argument(name="bar", help="string to print out again")
def foo2(bar: str):
    print(bar)

print(parser.execute("Parsegument group -help"), end="\n\n---\n\n")
print(parser.execute("Parsegument group foo -help"), end="\n\n---\n\n")
print(parser.execute("Parsegument group foo2 -help"), end="\n\n---\n\n")