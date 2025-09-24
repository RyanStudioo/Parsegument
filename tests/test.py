from parsegument import Parsegumenter

command = "customCommand subGroup arg \'someone or something space\' --yes -v"
test = Parsegumenter.parse_string(command)
print(test)