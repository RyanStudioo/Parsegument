
from parsegument.CommandGroup import CommandGroup
from parsegument.Command import Command
from parsegument.Arguments import Argument, Flag, Operand
from parsegument import Parsegumenter

def foo(bar, bar2, reverse:bool=False):
    if reverse:
        print(f"{bar} {bar2}"[::-1])
    print(bar, bar2)

def another(argument):
    print(argument[::-1])

parsegumenter = Parsegumenter()

main_command = CommandGroup("Main")
parsegumenter.add_child(main_command)

sub_command = CommandGroup("Sub")
main_command.add_child(sub_command)

command = Command("foo", foo)
sub_command.add_child(command)
command.add_node(Argument(name="bar", arg_type=str))
command.add_node(Argument(name="bar2", arg_type=str))
command.add_node(Flag(name="reverse"))

sub_sub_command = CommandGroup("SubSub")
sub_command.add_child(sub_sub_command)

another_command = Command("Another", another)
sub_sub_command.add_child(another_command)

parsegumenter.execute("Main Sub foo yes yes2")
parsegumenter.execute("Main Sub foo yes yes2 -reverse")
parsegumenter.execute("Main Sub SubSub Another yessir")


