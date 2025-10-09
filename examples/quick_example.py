import parsegument as pg

# function to execute
def adder(num1: float, num2: float) -> float:
    return num1 + num2

# Initialise Parsegumenter
parser = pg.Parsegumenter()

# Create a command group called pg
main_command = pg.CommandGroup(name="pg")
# Register the command group in Parsegumenter
parser.add_child(main_command)

# Create a command object and link it to the adder function
command = pg.Command(name="adder", executable=adder)
# Add the command to the "pg" command group
main_command.add_child(command)

# add the arguments to the command
command.add_node(pg.Argument("num1", float))
command.add_node(pg.Argument("num2", float))

# command to be parsed
command_string = "pg adder 10.3 20.4"
# Execute the command and print the result
result = parser.execute(command_string)
print(result)