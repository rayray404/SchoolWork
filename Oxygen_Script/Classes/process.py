class Stack:
    def __init__(self, stack):
        self.stack = stack
    def pop(self, condition=True):
        if condition:
            return(self.stack.pop())

    def push(self, element):
        self.stack.push()

class Processor:
    def __init__(self):
        stacks = []
        self.string_cache = dict()

    def process(self, expression):
        string_count = expression.count('"')
    
        for i in range(string_count//2):
            index1 = expression.index('"')
            index2 = expression[index1+1:].index('"')
            self.string_cache[len(self.string_cache)] = expression[index1+1:index2]
            expression = expression[:index1]+f'{ {len(self.string_cache)} }'.replace(' ', '') + expression[index2+1:]
            print(expression)
        
        return eval(" ".join(expression))