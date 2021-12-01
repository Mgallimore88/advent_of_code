class Instruction:
    def __init__(self, index, operation, argument):
        self.index = index
        self.operation = operation
        self.argument = argument
        self.number_of_times_called = 0
    
    def called_more_than_once(self):
        if self.number_of_times_called >1:
            return True
    
    def reset(self):
        self.number_of_times_called = 0
    