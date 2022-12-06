# solution to advent of code Dec 4 part 1
# https://adventofcode.com/2022/day/4


file = "input"

running_total = 0

def overlap(list_1, list_2):
    if any([item in list_1 for item in list_2]):
        return True


with open(file) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:
        area_a, area_b = line.split(",")

        start_a, end_a = area_a.split("-")
        area_a = range(int(start_a), int(end_a) + 1)

        start_b, end_b = area_b.split("-")
        area_b = range(int(start_b), int(end_b) + 1)

        if overlap(area_a, area_b) or overlap(area_b, area_a):
            running_total += 1
print(running_total)
