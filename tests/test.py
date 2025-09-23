from parsegument import Parsegumenter

command = "customCommand subGroup arg \"someone or something space\""
test = Parsegumenter.parse_string(command)
print(test)