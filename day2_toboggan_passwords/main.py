# read the file
with open("input") as file:
    raw = file.readlines()

# data cleaning
# initalize array of variables and populate with strings
# find integers of upper and lower bound for character frequency
# find check character
# find password
lowers = [""] * len(raw)
uppers = [""] * len(raw)
characters = [""] * len(raw)
passwords = [""] * len(raw)

for index, entry in enumerate(raw):
    lowers[index] = entry.split("-")[0]
    remainder = entry.split("-")[1]
    uppers[index] = remainder.split()[0]
    characters[index] = entry.split(":")[0][-1]
    passwords[index] = entry.split(":")[1][1:-1]


# check how many times the check character occurs for each entry
counts = [0] * len(raw)
total = 0

for index, password in enumerate(passwords):
    for letter in password:
        if letter == characters[index]:
            counts[index] += 1
print(f"count: {counts[0]}")

for index, count in enumerate(counts):
    if count >= int(lowers[index]) and count <= int(uppers[index]):
        total += 1

# test
print(f"lower {lowers[0]}")
print(f"upper {uppers[0]}")
print(f"char {characters[0]}")
print(f"password {passwords[0]}")
print(f"total valid passwords: {total}")
