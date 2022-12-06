# solution to advent of code Dec 5 part 1
# https://adventofcode.com/2022/day/4


stacks = {
    "stack_1": "FTCLRPGQ",
    "stack_2": "NQHWRFSJ",
    "stack_3": "FBHWPMQ",
    "stack_4": "VSTDF",
    "stack_5": "QLDWVFZ",
    "stack_6": "ZCLS",
    "stack_7": "ZBMVDF",
    "stack_8": "TJB",
    "stack_9": "QNBGLSPH",
}
# unpack from a string to a list so we can use pop()
for key in stacks:
    stacks[key] = [*stacks[key]]

file = "input"

with open(file) as f:
    lines = (line.rstrip() for line in f)

    # discard the first 10 lines
    for count in range(10):
        print(next(lines))

    # unpack the numbers
    for line in lines:
        n_moves, source, destination = [int(i) for i in line.split() if i.isdigit()]
        # move the crates around
        source_stack = stacks[f"stack_{source}"]
        dest_stack = stacks[f"stack_{destination}"]
        dest_stack.extend(source_stack[-n_moves:])
        for move in range(n_moves):
            try:
                source_stack.pop()
            except IndexError:
                continue


output = [stacks[stack].pop() for stack in stacks]

print("".join(output))
