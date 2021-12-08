import numpy as np

# Open the file
with open("input") as file:
    raw = [line.strip("\n") for line in file.readlines()]

# clean the data and get it into a numpy array for indexing
data = np.asarray([list(item) for item in raw], dtype=int)
print(data)

# count up all the ones in each column, and store the totals.
length_of_data = len(raw)
counts = [sum(data[:,n]) for n in range(len(data[0]))]

# divide the totals by the length of the array then round to nearest 0 or 1 
# to get binary representation. 
counts = np.divide(counts, length_of_data).round()

# convert to integers
gamma = np.asarray(counts, dtype=int)
# find the inverse of the 
epsilon = ~gamma+2

def clean_characters(input_string, list_of_chars):
    for char in list_of_chars:
        input_string = input_string.replace(char,"")
    return input_string

gamma = clean_characters(str(gamma),["[" , "]" ," " ])
epsilon = clean_characters(str(epsilon),["[" , "]" ," " ])


gamma_decimal = (int(gamma,2))
epsilon_decimal = (int(epsilon,2))

print(gamma_decimal * epsilon_decimal)
