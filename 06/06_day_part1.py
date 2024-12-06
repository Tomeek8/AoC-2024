import time


def parse(path):
    with open(path) as f:
        return [list(line) for line in f.read().splitlines()]


def starting_char(matrix):
    for char in "<>^v":
        for row in matrix:
            if char in row:
                return char


def start_position(char, matrix):
    for r, row in enumerate(matrix):
        if char in row:
            c = row.index(char)
            return (r, c)


def start_direction(char):
    match char:
        case ">":
            return (0, 1)
        case "<":
            return (0, -1)
        case "^":
            return (-1, 0)
        case "v":
            return (1, 0)


def move(r, c, direction):
    return r + direction[0], c + direction[1]


def obstacle_ahead(r, c, direction, matrix):
    ahead_r, ahead_c = move(r, c, direction)
    if ahead_r >= r_max or ahead_c >= c_max or ahead_r < 0 or ahead_c < 0:
        return False
    return matrix[ahead_r][ahead_c] == "#"


def turn_right(direction):
    return direction[1], -direction[0]


start_time = time.time()

matrix = parse("./06/sample.txt")
starting_char = starting_char(matrix)
r, c = start_position(starting_char, matrix)
direction = start_direction(starting_char)
r_max, c_max = len(matrix), len(matrix[0])
pos_visited = set()
inside = True

while inside:
    pos_visited.add((r, c))
    if obstacle_ahead(r, c, direction, matrix):
        direction = turn_right(direction)
    r, c = move(r, c, direction)
    if r >= r_max or c >= c_max or r < 0 or c < 0:
        inside = False

result1 = len(pos_visited)
print(f"Part 1 result: {result1}")
end_time = time.time()
print(f"Time: {end_time - start_time:.3f} s")
