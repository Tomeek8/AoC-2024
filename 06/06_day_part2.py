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


def obstacle_combinations(matrix):
    matrices = []
    for r, row in enumerate(matrix):
        for c, char in enumerate(row):
            if char == "#" or (r, c) == (49,47):
                continue
            new_matrix = [row.copy() for row in matrix]
            new_matrix[r][c] = "#"
            matrices.append(new_matrix)

    return matrices

start_time = time.time()

matrix = parse("./06/input.txt")
print(start_position("^", matrix))
start_char = starting_char(matrix)
r_max, c_max = len(matrix), len(matrix[0])

loops = 0
i_matrix = 0
for new_matrix in obstacle_combinations(matrix):
    # print(i_matrix)
    i_matrix += 1
    r, c = start_position(start_char, matrix)
    direction = start_direction(start_char)
    pos_visited = set()

    while True:
        pos_visited.add(((r, c), direction))
        if obstacle_ahead(r, c, direction, new_matrix):
            direction = turn_right(direction)
        else:
            r, c = move(r, c, direction)
        if r >= r_max or c >= c_max or r < 0 or c < 0:
            break
        if ((r, c), direction) in pos_visited:
            loops += 1
            break

print(f"Part 2 result: {loops}")
end_time = time.time()
print(f"Time: {end_time - start_time:.3f} s")
