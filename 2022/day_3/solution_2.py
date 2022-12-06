# solution to advent of code 3rd dec part 2
# https://adventofcode.com/2022/day/3#part2

# this challenge requires looking at the input in groups of three and finding the
# intersecting letter for each group.

file = "input"

lower_ASCII_start = 97
lower_ASCII_finish = 97 + 26
upper_ASCII_start = 65
upper_ASCII_finish = 65 + 26


alphabets = [chr(i) for i in range(lower_ASCII_start, lower_ASCII_finish)]
alphabets.extend([chr(i) for i in range(upper_ASCII_start, upper_ASCII_finish)])
scores = list(enumerate(alphabets, start=1))
scores = dict(reversed(score) for score in scores)

running_total = 0

with open(file) as f:
    lines = (line.rstrip() for line in f)
    lines_remain = True
    while lines_remain:
        try:
            first = next(lines)
            second = next(lines)
            third = next(lines)
            set_intersect = {*first} & {*second} & {*third}  # * means unpack
            running_total += scores[set_intersect.pop()]
        except StopIteration:
            lines_remain = False

print(running_total)
