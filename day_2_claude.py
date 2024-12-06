def check_increments(levels):
    if len(levels) < 2:
        return True

    diff = levels[1] - levels[0]
    if abs(diff) < 1 or abs(diff) > 3:
        return False

    increasing = diff > 0

    for i in range(2, len(levels)):
        new_diff = levels[i] - levels[i - 1]
        if (increasing and new_diff <= 0) or (not increasing and new_diff >= 0):
            return False
        if abs(new_diff) < 1 or abs(new_diff) > 3:
            return False

    return True


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if check_increments(levels):
            safe_count += 1
    return safe_count


# Read input from a file
with open("input2", "r") as file:
    reports = file.readlines()

# Remove any trailing newlines
reports = [report.strip() for report in reports]

# Count safe reports
result = count_safe_reports(reports)
print(f"Number of safe reports: {result}")


def check_increments(levels):
    if len(levels) < 2:
        return True

    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if i > 1 and ((diff > 0) != (levels[i - 1] - levels[i - 2] > 0)):
            return False

    return True


def is_safe_with_dampener(levels):
    if check_increments(levels):
        return True

    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i + 1 :]
        if check_increments(dampened_levels):
            return True

    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_with_dampener(levels):
            safe_count += 1
    return safe_count


# Read input from a file
with open("input2", "r") as file:
    reports = file.readlines()

# Remove any trailing newlines
reports = [report.strip() for report in reports]

# Count safe reports
result = count_safe_reports(reports)
print(f"Number of safe reports with Problem Dampener: {result}")
