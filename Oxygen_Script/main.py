from Classes.statements import *
from Classes.types import type_cast
from Classes.process import Processor

variables = dict()

code_file = open("file.oxy", "r")
code_read = code_file.read()
code_file.close()

code = code_read.split('\n')
processors = [Processor()]

for i in code:
    statement = i.split(' ')
    match i[-1]:
        case '?':
            this = Question(statement[0], processors[0])
            variables[statement[2]] = type_cast(this.command(statement[3:-1]), statement[1])
        
        case '.':
            this = Declaration(statement[1], processors[0])
            variables[statement[0]] = type_cast(this.command(statement[3:-1]), statement[2])
        
        case '!':
            this = Exclamation(statement[0], processors[0])
            this.command(statement[1:-1])

print(variables)