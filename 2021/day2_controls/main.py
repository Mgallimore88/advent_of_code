# open the file
with open("input") as file:
    raw = file.readlines()
movements = [line.strip("\n") for line in raw]

# make some variables
forwards = 0
ups = 0
downs = 0

# make some functions
def word_part(move):
    word = move.split(" ")[0]
    return word


def number_part(move):
    number = move.split(" ")[1]
    return int(number)

# check how far the submarine moved and increment
for move in movements:
    if word_part(move) == "forward":
        forwards += number_part(move)
    elif word_part(move) == "up":
        ups += number_part(move)
    elif word_part(move) == "down":
        downs += number_part(move)

# note the minus sign for ups - these decrease the depth
depth = downs - ups

print(depth * forwards)
