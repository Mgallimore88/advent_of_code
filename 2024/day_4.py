# part 1

import numpy as np
import re


# 1. read the input
def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        return lines


input = read_input("input4")
list_of_lines = [l[:-1] for l in input]

# 2. Make a matrix from the input
matrix = np.array([list(row) for row in list_of_lines])


# 3. find the occurence of a pattern in each row of the matrix
pattern = "XMAS"

def count_matches(mat, pattern=pattern):
    all_matches = []
    for row in mat:
        string = "".join(row)
        matches = re.findall(pattern, string)
        all_matches += matches
    return len(all_matches)


# 4. Define the transforms
def x_transform(mat):
    return np.fliplr(mat)


def y_transform(mat):
    return np.flipud(mat)


def diagonal_transform(mat):
    # k is the distance from the diagonal at 0,0
    len_x = len(mat[0, :])
    len_y = len(mat[:, 0])
    diagonals = [np.diag(mat, k) for k in range(-len_y, len_x)]
    return diagonals


def rotate_90_ccw(mat):
    return np.rot90(mat)

# 5. Perform all eight possible transforms and find the pattern matches in each of the resulting matrices.

# East
matches = count_matches(matrix)
# South East
matches += count_matches(diagonal_transform(matrix))
# South
matches += count_matches(rotate_90_ccw(matrix))
# South West
matches += count_matches(diagonal_transform(x_transform(matrix)))
# West
matches += count_matches(x_transform(matrix))
# North West
matches += count_matches(diagonal_transform(x_transform(y_transform(matrix))))
# North: apply 90 degree ccw transform 3 times to get 270 degrees
matches += count_matches(rotate_90_ccw(rotate_90_ccw(rotate_90_ccw(matrix))))
# North East
matches += count_matches(diagonal_transform(y_transform(matrix)))

print("part 1")
print(matches)

# Part 2
# Make a 9 x 9 kernel which iterates along the matrix printing out each possible 9x9 grid
kernel = np.array([1,1,1], [1,1,1], [1,1,1])

def sliding_window()


# Return the ones where the centre cell is "A"