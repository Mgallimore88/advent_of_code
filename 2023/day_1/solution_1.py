file = "input.txt"

with open(file) as f:
    lines = (line.rstrip() for line in f)

    total = int(0)

    for line in lines:
        print(line)
        nums = [int(s) for s in list(line) if s.isdigit()]
        last = nums[-1]
        first = nums[0]
        concat = int(str(first) + str(last))

        total += concat

        print(total)
