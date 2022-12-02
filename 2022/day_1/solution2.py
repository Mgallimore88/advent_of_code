# solution to advent of code 1st dec part 2

file = "input"

max_cals = 0
running_total = 0
running_totals = []

# This approach makes a list of totals, then sorts them to find the highest 3 values. 
with open(file) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:
        if len(line) > 0:
            running_total += int(line)
        else:
            running_totals.append(running_total)
            running_total = 0 #reset

print(sum(sorted(running_totals)[-3:]))
