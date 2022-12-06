# solution to advent of code Dec 6 part 2
# https://adventofcode.com/2022/day/6


file = "input"

buffer_length = 14


def increment_buffer(buffer, new_item, length):
    for n in range(length - 1):
        buffer[n] = buffer[n + 1]
    buffer[length - 1] = new_item


with open(file) as f:
    character_gen = (chars for chars in f.read())

    # get the first 4 characters
    four_char_buffer = [next(character_gen) for i in range(buffer_length)]

    index = 14
    start_of_packet_markers = []

    if len(set(four_char_buffer)) == buffer_length:
        start_of_packet_markers.append(index)

    # iterate over the remaining characters
    for next_char in character_gen:
        increment_buffer(four_char_buffer, next_char, buffer_length)
        index += 1

        # check for repeating characters in buffer
        if len(set(four_char_buffer)) == buffer_length:
            start_of_packet_markers.append(index)


print(start_of_packet_markers)
