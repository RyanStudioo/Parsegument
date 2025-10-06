from typing import Union
import parsegument as pg


def example_function(string_arg: str, int_arg: int, to_print:bool=False, extra_value:float=10.0) -> str:
    if to_print:
        print(string_arg, int_arg, "printed")
    return f"{string_arg} {int_arg} {extra_value}"

parser = pg.Parsegumenter()

main = pg.CommandGroup("main")
parser.add_child(main)

command = pg.Command("sub", example_function)
main.add_child(command)

command.add_node(pg.Argument("string_arg", str))
command.add_node(pg.Argument("int_arg", int))
command.add_node(pg.Flag("to_print"))

print(parser.execute("main sub yes 10"))
print(parser.execute("main sub yes 10 -to_print"))
print(parser.execute("main sub yes 10 --extra_value=11.9"))
