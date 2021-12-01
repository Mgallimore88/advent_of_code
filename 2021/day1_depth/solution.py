# solution to advent of code 1st dec part 1
# open and clean the file
with open("input") as f:
    depths = f.readlines()
depths = [int(line.strip("\n")) for line in depths]

# make a variable to count increments
increments = 0
current_depth = depths[0]

# loop through to check whether increment or decrement
for new_depth in depths[1:]:
    if (new_depth) > (current_depth):
        increments += 1
    current_depth = new_depth

print(increments)
