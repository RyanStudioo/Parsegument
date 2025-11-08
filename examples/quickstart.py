import parsegument as pg
parser = pg.Parsegumenter(name="quickstart") # Create Parsegumenter

@parser.command() # Add decorator to create command
def foo(bar:str):
    print(bar)

parser.execute("quickstart foo bar_string") # Execute string