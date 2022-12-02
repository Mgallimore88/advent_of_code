# solution to advent of code 2nd dec part 1

file = "input"
running_total = 0

throw_scores = {"X": 1, "Y": 2, "Z": 3}
win_scores = {
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

        win_score = win_scores[opponent + response]
        throw_score = throw_scores[response]

        running_total += win_score + throw_score
print(running_total)
