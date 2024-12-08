from itertools import combinations
from collections import defaultdict
import time


def parse(path):
    with open(path) as f:
        return [list(line.strip()) for line in f]


def is_inside(position, matrix):
    r, c = position
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])


def antennas_positions(matrix):
    ap = defaultdict(set)
    for r, row in enumerate(matrix):
        for c, char in enumerate(row):
            if char not in "#.":
                ap[char].add((r, c))
    return ap


def get_antinode_positions(pos1, pos2):
    vector = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    an1 = (pos1[0] - vector[0], pos1[1] - vector[1])
    an2 = (pos2[0] + vector[0], pos2[1] + vector[1])
    return an1, an2


def part1():
    matrix = parse("./08/input.txt")
    antinodes_positions = set()
    for antenna, positions in antennas_positions(matrix).items():
        for combination in combinations(positions, 2):
            an1, an2 = get_antinode_positions(combination[0], combination[1])
            if is_inside(an1, matrix):
                antinodes_positions.add(an1)
            if is_inside(an2, matrix):
                antinodes_positions.add(an2)
    return len(antinodes_positions)


start_time = time.time()
print(f"Part 1 result: {part1()}")
print(f"Time: {time.time() - start_time:.3f} s")
