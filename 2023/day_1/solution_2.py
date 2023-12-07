file = "input.txt"

word_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

number_words = word_to_num.keys()


class NumberTracker:
    """
    Keeps track of the numbers and their index along the string.
    The numbers are stored as strings for easier concatenation.
    """

    def __init__(self):
        self.item_dict = {}

    def add(self, index: int, number: str):
        if number.isdigit():
            self.item_dict[index] = number
        elif number.isalpha():
            self.item_dict[index] = word_to_num[number]

    def get_first(self):
        min_idx = min(self.item_dict.keys())
        return self.item_dict[min_idx]

    def get_last(self):
        max_idx = max(self.item_dict.keys())
        return self.item_dict[max_idx]


with open(file) as f:
    lines = (line.rstrip() for line in f)

    total = int(0)

    for line in lines:
        tracker = NumberTracker()

        # First deal with the numeric characters like '1'.
        positions = [pair for pair in list(enumerate(line)) if pair[1].isdigit()]

        # only add numbers from the line if there were some.
        if positions:
            for idx, num in positions:
                tracker.add(idx, num)
        positions = []

        # Second deal with the spelled numbers like 'one'.
        # Number-words might occur more than once per line, so add each one until there are none left.
        for word in number_words:
            idx = 0
            word_length = len(word)

            while word in line[idx:]:
                # find index of start of word
                # add to tracker
                # move index past end of word
                idx += line[idx:].find(word)
                tracker.add(idx, word)
                idx += word_length

        first = tracker.get_first()
        last = tracker.get_last()
        concat = int(str(first) + str(last))
        total += concat
        print(total)
