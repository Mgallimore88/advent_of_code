def get_lines(file="input"):
    with open(file) as f:
    lines = (line.rstrip() for line in f)
    return lines