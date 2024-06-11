
class Question:
    def __init__(self, command, processor):
        self.command = {'take':self.take}[command]
        self.processor = processor
    
    def take(self, prompt):
        print(self.processor.process(prompt), end="")
        inp = input()
        return inp
        
class Exclamation:
    def __init__(self, command, processor):
        self.command = {'shomme':self.output}[command]
        self.processor = processor
    
    def output(self, prompt):
        print(self.processor.process(prompt), end="")

class Declaration:
    def __init__(self, command, processor):
        self.command = {'is': self._is}[command]
        self.processor = processor
    
    def _is(self, prompt):
        return self.processor.process(prompt)
    
