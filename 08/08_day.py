from itertools import combinations
from collections import defaultdict
import time


def parse(path):
    with open(path) as f:
        return [list(line.strip()) for line in f]


def is_inside(position, r_max, c_max):
    r, c = position
    return 0 <= r < r_max and 0 <= c < c_max


def antennas_positions(matrix):
    ap = defaultdict(set)
    for r, row in enumerate(matrix):
        for c, char in enumerate(row):
            if char not in "#.":
                ap[char].add((r, c))
    return ap


def antinode_generator(pos1, pos2):
    vector = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    while True:
        antinode_position = (pos2[0] + vector[0], pos2[1] + vector[1])
        yield antinode_position
        pos2 = antinode_position


def get_antinode_positions(pos1, pos2, r_max, c_max, multinodes_allowed=False):
    antinodes = set()
    gen1 = antinode_generator(pos1, pos2)
    gen2 = antinode_generator(pos2, pos1)
    if not multinodes_allowed:
        an1 = next(gen1)
        an2 = next(gen2)
        if is_inside(an1, r_max, c_max):
            antinodes.add(an1)
        if is_inside(an2, r_max, c_max):
            antinodes.add(an2)
        return antinodes
    while True:
        an1 = next(gen1)
        if is_inside(an1, r_max, c_max):
            antinodes.add(an1)
        else:
            break
    while True:
        an2 = next(gen2)
        if is_inside(an2, r_max, c_max):
            antinodes.add(an2)
        else:
            break
    return antinodes


def main(multinodes_allowed=False):
    matrix = parse("./08/input.txt")
    r_max, c_max = len(matrix), len(matrix[0])
    antinodes = set()
    for positions in antennas_positions(matrix).values():
        for combination in combinations(positions, 2):
            pos1, pos2 = combination
            antinodes.update(
                get_antinode_positions(pos1, pos2, r_max, c_max, multinodes_allowed)
            )
    if not multinodes_allowed:
        return len(antinodes)
    for positions in antennas_positions(matrix).values():
        if len(positions) > 1:
            antinodes.update(positions)
    return len(antinodes)


start_time = time.time()
print(f"Part 1 result: {main()}")
print(f"Part 2 result: {main(multinodes_allowed=True) }")
print(f"Time: {time.time() - start_time:.3f} s")
