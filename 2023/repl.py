line = "npfdbnjlthree6cmdbsrsqc9five"
word = "three"

idx = 0
word_length = len(word)
while word in line[idx:]:  # when does the argument of while loop get updated?
    print(word)
    print(line[idx:])
    idx = line[idx:].find(word)
    print(idx)
    idx += word_length
