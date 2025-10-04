from parsegument.CommandGroup import CommandGroup
from parsegument.Command import Command
from src.parsegument import Parsegumenter

def foo(bar):
    print(bar)

parsegumenter = Parsegumenter()
main_command = CommandGroup("Main")
sub_command = CommandGroup("Sub")
command = Command("foo", foo)
main_command.add_child(sub_command)
sub_command.add_child(command)
parsegumenter.add_child(main_command)

parsegumenter.execute("Main Sub foo yes")

