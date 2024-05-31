class Question:
    def __init__(self, command):
        self.command = {'take':self.take}[command]
    
    def take(self, prompt):
        return input(" ".join(prompt))

class Exclamation:
    def __init__(self):
        pass

class Sentence:
    def __init__(self):
        pass