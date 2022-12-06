# solution to advent of code 3rd dec part 1
# https://adventofcode.com/2022/day/3

file = "input"


def bisect(items: str):
    split_index = int(len(items) / 2)
    first_half = items[:split_index]
    second_half = items[split_index:]
    return first_half, second_half


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
    for line in lines:
        first, second = bisect(line)
        set_intersect = {*first} & {*second}  # * means unpack
        running_total += scores[set_intersect.pop()]
print(running_total)
