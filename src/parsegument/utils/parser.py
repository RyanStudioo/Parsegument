<<<<<<< HEAD
import re
=======
>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017

def parse_string(string:str) -> list:
    if not string: return []
    opened_quotation = False
    saved_index = 0
    arguments = []
    for idx, letter in enumerate(string):
        if letter == '"' or letter == "'":
            opened_quotation = not opened_quotation
            if opened_quotation:
                saved_index = idx+1
            else:
                arguments.append(string[saved_index:idx])
                saved_index = idx + 1
            continue
        if letter == ' ' and not opened_quotation:
            arguments.append(string[saved_index:idx])
            saved_index = idx + 1
            continue
    if string[saved_index:]:
        arguments.append(string[saved_index:])
    return arguments

<<<<<<< HEAD
def node_type(node:str):
    if node[0] == "-":
        if node[1] == "-":
            return "Operand"
        return "Flag"
    return "Argument"

def parse_operand(operand:str):
    value = re.search("=.*", operand)
    return value.group()[1:] if value else None
=======
>>>>>>> 69282319c164e3f2bf48fabf38a42a335ff61017

