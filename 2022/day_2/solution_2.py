# solution to advent of code 2nd dec part 2


file = "input"
running_total = 0

throw_scores = {"rock": 1, "paper": 2, "scissors": 3}

win_scores = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

throw_decider = {
    "AX": "scissors",
    "AY": "rock",
    "AZ": "paper",
    "BX": "rock",
    "BY": "paper",
    "BZ": "scissors",
    "CX": "paper",
    "CY": "scissors",
    "CZ": "rock",
}

with open(file) as f:
    rounds = (line.rstrip() for line in f)
    for round in rounds:
        opponent = round[0]
        strategy = round[2]
        response = throw_decider[opponent + strategy]

        win_score = win_scores[strategy]
        throw_score = throw_scores[response]

        running_total += throw_score + win_score

print(running_total)
