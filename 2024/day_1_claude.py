def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the distance for each pair and sum
    total_distance = sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

    return total_distance


# Read input
left_list = []
right_list = []

# You might need to adjust this part depending on how your input is formatted
with open("input1a", "r") as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Calculate and print the result
result = calculate_total_distance(left_list, right_list)
print(f"The total distance between the lists is: {result}")

# part 2

from collections import Counter


def calculate_similarity_score(left_list, right_list):
    # Create a frequency count of numbers in the right list
    right_counter = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counter[num] for num in left_list)

    return similarity_score


# Read input
left_list = []
right_list = []

# You might need to adjust this part depending on how your input is formatted
with open("input1a", "r") as file:
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Calculate and print the result
result = calculate_similarity_score(left_list, right_list)
print(f"The similarity score between the lists is: {result}")
