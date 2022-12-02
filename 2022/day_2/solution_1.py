# solution to advent of code 2nd dec part 1

file = "input"
running_total = 0

score_dict = {"X": 1, "Y": 2, "Z": 3}
win_dict = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


with open(file) as f:
    lines = (line.rstrip() for line in f)
    for line in lines:
        opponent = line[0]
        response = line[2]

        results = win_dict[opponent + response]
        throws = score_dict[response]

        running_total += results + throws
print(running_total)
