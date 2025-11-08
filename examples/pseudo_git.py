# initialising
import parsegument as pg

parser = pg.Parsegumenter(
    name="git",
    help="An imitation of git using Parsegument"
)


@parser.command(help="Add a file")
@pg.argument("file", help="The file to add")
def add(file: str):
    print("files added:", file)

@parser.command(help="Remove a file")
@pg.argument("file", help="The file to remove")
def remove(file: str):
    print("files removed:", file)

@parser.command(help="Commit to git")
def commit(message: str=""):
    print("Committed with the following message:", message)

@parser.command(help="Push to repo")
def push():
    print("Pushed to repo")

print(parser.execute("git -help"))
print(parser.execute("git add --help"))

parser.execute("git add script.py")
parser.execute("git commit --message='new file'")
parser.execute("git push")