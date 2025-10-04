<<<<<<< HEAD
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

=======
from parsegument import Parsegumenter

command = "customCommand subGroup arg \"someone or something space\""
test = Parsegumenter.parse_string(command)
print(test)
>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017
