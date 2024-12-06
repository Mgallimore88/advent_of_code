from collections import Counter


def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
        # content = [x.strip() for x in content]
    return content


content = read_file("input1a")

firsts = []
seconds = []

for line in content:
    first = int(line.split()[0])
    second = int(line.split()[1])
    firsts.append(first)
    seconds.append(second)

firsts.sort()
seconds.sort()

difference = 0
for pair in zip(firsts, seconds):
    difference += abs(pair[0] - pair[1])

print("part 1")
print(difference)


# Part 2

distance = 0
c = Counter(seconds)
for i in set(firsts):
    distance += i * c[i]

print("part 2")
print(distance)
