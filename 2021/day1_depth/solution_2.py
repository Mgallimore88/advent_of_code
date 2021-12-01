# solution to advent of code 1st dec part 2

# open and clean the file
with open("input") as f:
    depths = f.readlines()
depths = [int(line.strip("\n")) for line in depths]

# make variables to count increments and store depth window
increments = 0
current_window = [depths[0], depths[1], depths[2]]

# loop through to check whether increment or decrement
# start at index 3 since 0,1,2 are first window.
for depth in depths[3:]:
    next_window = [current_window[1], current_window[2], depth]
    if sum(next_window) > sum(current_window):
        increments += 1
    current_window = next_window

print(increments)
