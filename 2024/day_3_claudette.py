import re


def process_memory(memory):
    # Regex pattern to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    total_sum = 0

    # Find all matches
    matches = re.finditer(pattern, memory)

    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        result = num1 * num2
        total_sum += result
        print(f"Found: mul({num1},{num2}) = {result}")

    return total_sum


# Example usage
with open("input3") as f:
    memory = f.read()
result = process_memory(memory)
print(f"Total sum: {result}")

import re


def process_memory(memory):
    # Regex patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    total_sum = 0
    mul_enabled = True  # Multiplication is enabled at the start

    # Combine all patterns
    combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"

    # Find all matches
    matches = re.finditer(combined_pattern, memory)

    for match in matches:
        if match.group(0).startswith("mul"):
            if mul_enabled:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                result = num1 * num2
                total_sum += result
                print(f"Executed: mul({num1},{num2}) = {result}")
            else:
                print(f"Skipped: {match.group(0)} (multiplication disabled)")
        elif match.group(0) == "do()":
            mul_enabled = True
            print("Multiplication enabled")
        elif match.group(0) == "don't()":
            mul_enabled = False
            print("Multiplication disabled")

    return total_sum


# Example usage
result = process_memory(memory)
print(f"Total sum: {result}")
