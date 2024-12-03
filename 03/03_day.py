import re

with open("input.txt") as f:
    text = f.read()


def part1(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)
    return sum(int(nums[0]) * int(nums[1]) for nums in matches)


def part2(text):
    pattern2 = r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))"
    matches = re.findall(pattern2, text)
    enabled = True
    enabled_matches = []
    for match in matches:
        if match not in {"don't()", "do()"} and enabled:
            enabled_matches.append(match)
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
    return part1("".join(enabled_matches))


print(f"Part 1 result: {part1(text)}")
print(f"Part 2 result: {part2(text)}")
