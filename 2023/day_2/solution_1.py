file = "input"

available_reds = 12
available_greens = 13
available_blues = 14


total = 0


def reset_colours():
    return 0, 0, 0


reds, greens, blues = reset_colours()


def get_digits(string):
    digits = [int(s) for s in string if s.isdigit()]
    # join all the digits into a single string
    return int("".join(str(d) for d in digits))


def get_colour(draw, colour):
    group = draw.split(",")
    return [item for item in group if colour in item][0]


def get_colours(draw, colour):
    if colour in draw:
        return get_digits(get_colour(draw, colour))
    else:
        return 0


with open(file) as f:
    lines = (line.rstrip() for line in f)

    for line in lines:
        game_number = get_digits(line.split(":")[0])
        game = line.split(":")[1]
        print(game_number)
        draws = game.split(";")
        for draw in draws:
            reds += get_colours(draw, "red")
            greens += get_colours(draw, "green")
            blues += get_colours(draw, "blue")

        if (
            reds < available_reds
            and greens < available_greens
            and blues < available_blues
        ):
            total += game_number

        print(reds, greens, blues)
        print(total)
