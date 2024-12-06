import numpy as np


# functions to check if the numbers are safe
def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return content


def safe_increment_magnitude(numbers: list, min: int = 1, max: int = 3) -> bool:
    diffs = np.diff(numbers)
    safe = True
    for n in diffs:
        if abs(n) < min:
            safe = False
        if abs(n) > max:
            safe = False
    return safe


def sign(number: int):
    return -1 if number < 0 else 1


def continuous_increment_direction(numbers: list) -> bool:
    signs = []
    diffs = np.diff(numbers)
    for number in diffs:
        signs.append(sign(number))

    return len(set(signs)) == 1


def check_safety(content: list):

    counts = 0
    for idx, line in enumerate(content):
        numbers = [int(x) for x in line.split()]
        safe_bool = safe_increment_magnitude(
            numbers
        ) and continuous_increment_direction(numbers)
        content[idx] = content[idx] + str(safe_bool)
        counts += safe_bool
    return content, counts


def check_increments(input):
    return safe_increment_magnitude(input) and continuous_increment_direction(input)


def drop_each_number_and_check_safety(content: list) -> tuple[list, int]:
    safe = False
    counts = 0
    for line_idx, line in enumerate(content):
        numbers = [int(x) for x in line.split()]
        originals = tuple(numbers)
        for idx, _ in enumerate(numbers):
            modified_numbers = numbers[:idx] + numbers[idx + 1 :]
            safe = check_increments(modified_numbers) or check_increments(
                list(originals)
            )
            if safe:
                content[line_idx] = content[line_idx] + str(safe)
                counts += safe
                break
            elif not safe:
                numbers = list(originals)
                continue

    return content, counts


# part 1
print("part 1")
content = read_file("input2")
content, counts = check_safety(content)
print(content)
print(counts)

# part 2
content = read_file("input2")
content, counts = drop_each_number_and_check_safety(content)
print(content)
print("part 2")
print(counts)
