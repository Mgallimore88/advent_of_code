# solution to advent of code 1st dec part 1
# This approach uses a generator to check each total one by one, 
# replacing the current max total whenever the running total is larger. 

file = "input"

max_cals = 0
running_total = 0


def update_max(current, max):
    if current > max:
        max = current
    return max


with open(file) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:
        if len(line) > 0:
            running_total += int(line)
        else:
            max_cals = update_max(running_total, max_cals)
            running_total = 0

print(max_cals)
