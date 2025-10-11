import shlex

import parsegument as pg


parser = pg.Parsegumenter()
group = pg.CommandGroup("test")
parser.add_child(group)

@group.command
def check_type(foo: str, bar: str, test: int=1, test2: float=2.0):
    print(type(foo), type(bar), type(test), type(test2))

testcases = [
    'test check_type yes something',
    'test check_type idkbruh yes --test=4',
    'test check_type something yes --test2=3.9',
]


for cases in testcases:
    parser.execute(cases)