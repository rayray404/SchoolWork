from Classes.statements import *
from Classes.types import type_cast

variables = dict()

code_file = open("file.oxy", "r")
code_read = code_file.read()
code_file.close()

code = code_read.split('\n')

for i in code:
    statement = i.split(' ')
    match i[-1]:
        case '?':
            this = Question(statement[0])
            variables[statement[2]] = type_cast(this.command(statement[3:-1]), statement[1])
print(variables)
print(code)