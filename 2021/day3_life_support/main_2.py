import numpy as np

# Open the file
with open("input") as file:
    raw = [line.strip("\n") for line in file.readlines()]

# clean the data and get it into a numpy array for indexing
data = np.asarray([list(item) for item in raw], dtype=int)
print(data)


def clean_characters(input_string, list_of_chars):
    for char in list_of_chars:
        input_string = input_string.replace(char, "")
    return input_string


print(len(data))

# recursive function to test for all the conditions specified in day3 part 2:
# The function looks at the length of an input numpy array of bitstrings 
# and compares the frequency of the nth element of each list item, whittling 
# down the list according to a comparison of the frequency of the nth elements, 
# with the list item's nth element. Currently not running. 

def reduce(data, iterator, mode):
    reduced = data
    print(reduced)
    print(len(data))
    if len(data) > 1:
        data = np.array(data)
        count_ones = sum(data[:, iterator])
        count_zeros = len(data) - count_ones

        comparison_bit = 1

        if mode == "most":
            if count_zeros < count_ones:
                comparison_bit = 0

        elif mode == "least":
            if count_zeros <= count_ones:
                comparison_bit = 0

        reduced = []
        for entry in data:
            if entry[iterator] == comparison_bit:
                reduced.append(list(entry))

        iterator += 1
        return reduce(reduced, iterator, mode)

    elif len(data) == 1:
        print(data)
        return data


oxy = str(reduce(data, 0, "most"))
co2 = str(reduce(data, 0, "least"))

oxy = clean_characters(oxy, ["[", ",", " ", "]"])
co2 = clean_characters(co2, ["[", ",", " ", "]"])

oxy = int(oxy, 2)
co2 = int(co2, 2)

print(oxy * co2)
