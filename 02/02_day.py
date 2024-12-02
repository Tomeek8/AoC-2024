with open("./02/input.txt") as f:
    lines = [list(map(int, line.split())) for line in f]


def check_differences(line):
    for i in range(len(line) - 1):
        diff = abs(line[i + 1] - line[i])
        if diff > 3 or diff == 0:
            return False
    return True


def check_sorted(line):
    return line == sorted(line) or line == sorted(line, reverse=True)


def one_out_combinations(line):
    combinations = []
    for i in range(len(line)):
        combinations.append(line[:i] + line[i + 1 :])
    return combinations


def check_lines_part_1(lines):
    safe_reports = 0
    for line in lines:
        if check_differences(line) and check_sorted(line):
            safe_reports += 1
    return safe_reports


def check_lines_part_2(lines):
    safe_reports = 0
    for line in lines:
        if check_differences(line) and check_sorted(line):
            safe_reports += 1
        else:
            for combination in one_out_combinations(line):
                if check_differences(combination) and check_sorted(combination):
                    safe_reports += 1
                    break
    return safe_reports


print(check_lines_part_1(lines))
print(check_lines_part_2(lines))
