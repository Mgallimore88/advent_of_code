file = "input"


# need to make a function similar to isdigit, but for the list of words contained in this dict:

number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_highest_key(dict):
    return max(dict.keys())


def get_lowest_key(dict):
    # if not -1
    try:
        return min([k for k in dict.keys() if k != -1])
    except:
        return None


with open(file) as f:
    lines = (line.rstrip() for line in f)

    total = int(0)

    for line in lines:
        print(line)
        nums = [int(s) for s in list(line) if s.isdigit()]

        last_num = nums[-1]
        last_num_idx = line.find(str(last_num))

        first_num = nums[0]
        first_num_idx = line.find(str(first_num))

        word_idx_dict = {}
        for word in number_words:
            print(word)
            print(line.find(word))
            word_idx_dict[line.find(word)] = word

        first_num_word = word_idx_dict[get_lowest_key(word_idx_dict)]
        last_num_word = word_idx_dict[get_highest_key(word_idx_dict)]

        print(first_num_word)
        print(last_num_word)

        # concat = int(str(first) + str(last))
