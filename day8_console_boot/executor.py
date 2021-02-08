class Executor:
    def __init__(self, instruction):
        self.operation = instruction.operation
        self.argument = int(instruction.argument)