# open the file
with open("input") as file:
    raw = file.readlines()
movements = [line.strip("\n") for line in raw]


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def update(self, word, number):
        if word == "forward":
            self.horizontal += number
            self.depth += self.aim * number
        elif word == "up":
            self.aim -= number
        elif word == "down":
            self.aim += number


def word_part(move):
    word = move.split(" ")[0]
    return word


def number_part(move):
    number = move.split(" ")[1]
    return int(number)


sub = Submarine()

for move in movements:
    sub.update(word_part(move), number_part(move))

print(sub.horizontal * sub.depth)
