# This script looks through a list of numbers to find the two 
# which sum to 2020, then multiplies them and outputs the result. 


# find the two numbers in a list which add to 2020

# open the file and see each entry as a new list item
with open("input") as file:
    raw = file.readlines()

# convert the strings to integers and drop the final two characters (\n)
for index, entry in enumerate(raw):
    raw[index] = int(entry[:-1])

# do the comparison for each item in the list - could be more efficient but it works.
for i in raw:
    for j in raw:
        if i + j == 2020:
            print(f'2 components: {i}  and {j}')
            print(f'product: {i*j}')

######## Part 2 #########
# which three numbers from the input list add to 2020?

for i in raw:
    for j in raw:
        for k in raw:
            if i + j + k == 2020:
                print(f' three components: {i, j, k}')
                print(f'product: {i * j * k}')
