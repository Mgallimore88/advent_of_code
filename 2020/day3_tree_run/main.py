# read the file

with open("input") as file:
    raw = file.readlines()

# clean the newlines off the ends of the lines
cleaned = [0] * len(raw)
for index, line in enumerate(raw):
    cleaned[index] = line[:-1]


# initialize, check path and count encounters
right = 0
down = 0
tree_count = 0
print(cleaned)
for step in cleaned:
    if cleaned[down][right % 31] == "#":
        tree_count += 1
    right += 3
    down += 1
print(f"Trees encountered part 1 = {tree_count}")

# had the right idea but wasted a lot of time by not noticing that the \n escape character is treated as one chartacter by python,
# and by not noticing that each line was 31 characters long, thought it was 30 because I cut the last 2 characters off each line
# because of the \n thing. Also I was incrementing across and down before checking equality =='#' which was causing index out of
# range error.

# in part 2 I wasted time after renaming a variable from 'across' to 'right' and not renaming all the variables.

# part 2
right = 0
down = 0
tree_count = 0


trees = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope in slopes:
    for i in cleaned:
        if down <= len(
            cleaned
        ):  # this is so the final slope doesn't index out of the array
            if cleaned[down][right % 31] == "#":
                tree_count += 1
            right += slope[0]
            down += slope[1]
    trees.append(tree_count)
    right = 0
    down = 0
    tree_count = 0


def list_product(input):
    product = 1
    for item in input:
        product *= item
    if len(input) == 0:
        return 0
    else:
        return product


print(f"trees encountered part 2 = {trees}")
product = list_product(trees)
print(f"product = {product}")
