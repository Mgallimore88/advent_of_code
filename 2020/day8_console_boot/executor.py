class Executor:
    def __init__(self, instruction):
        try:
            self.operation = instruction.operation
            self.argument = int(instruction.argument)
        except:
            print("Executor encountered empty line! \nAssuming end of file has been reached.")
            self.operation = None
            self.argument = None