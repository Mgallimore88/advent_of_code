import re

with open("input3") as f:
    lines = f.read()

print(lines)

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, lines)
print(matches)

sum = 0
for match in matches:
    num1, num2 = map(int, match)
    mul = num1 * num2
    sum += mul
print(sum)

# part 2


def find_mul_expressions(text: str, word1, word2):

    last_word1_pos = -1
    last_word2_pos = -1
    entries = []

    for match in re.finditer(pattern, lines):
        num1, num2 = map(int, match.groups())
        word1_pos = text.rfind(word1, last_word1_pos + 1, match.start())
        word2_pos = text.rfind(word2, last_word2_pos + 1, match.start())
        entries.append([word1_pos, word2_pos, num1, num2])
    return entries


results = find_mul_expressions(lines, "do()", "don't()")
print(results)

sum = 0
for line in results:
    if line[1] > line[0]:  # means don't is after do
        continue
    if (line[0] > line[1]) or (
        line[0] == -1 and line[1] == -1
    ):  # means do is after don't or both are not present
        sum += line[2] * line[3]
print(sum)
