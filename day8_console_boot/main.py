from instruction import Instruction
from executor import Executor

# read the input file
with open("input") as file:
    raw = file.read()

cleaned = raw.split("\n")
instructions = {}

for index, instruction in enumerate(cleaned):
    instructions[index] = Instruction(index, instruction[:3], instruction[4:])

print(instructions[4].argument)
global_accumulator = 0
no_repeated_instructions = True
instruction_index = 0

while no_repeated_instructions:

    # increment instruction counter and check for repeats
    instructions[instruction_index].number_of_times_called += 1
    if instructions[instruction_index].called_more_than_once():
        no_repeated_instructions = False
        continue

    # load current instruction and perform operations
    current = Executor(instructions[instruction_index])
    if current.operation == "acc":
        global_accumulator += current.argument
        print(global_accumulator)
        instruction_index += 1
        print(f"acc {current.argument} index {instruction_index}")
    elif current.operation == "jmp":
        instruction_index += current.argument
        print(f"jmp {current.argument} index {instruction_index}")
    elif current.operation == "nop":
        print(f"nop, index {instruction_index}")
        instruction_index += 1

print(f"global accumulator = {global_accumulator}")


##### try using recursion to do part 2