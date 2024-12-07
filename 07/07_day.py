def parse(path):
    with open(path) as f:
        return [
            (
                int(line.split(": ")[0]),
                list(map(int, (line.split(": ")[1].strip().split(" ")))),
            )
            for line in f.read().splitlines()
        ]


def is_equation_valid(test_value, numbers, part=1):
    partial_sums = [numbers[0]]
    for num in numbers[1:]:
        new_partial_sums = []
        for partial_sum in partial_sums:
            new_partial_sums.append(partial_sum + num)
            new_partial_sums.append(partial_sum * num)
            if part == 2:
                new_partial_sums.append(int(f"{partial_sum}{num}"))
        partial_sums = new_partial_sums
    return test_value in partial_sums


def get_result(part=1):
    data = parse("./07/input.txt")
    test_values_passed = []
    for test_value, numbers in data:
        if is_equation_valid(test_value, numbers, part):
            test_values_passed.append(test_value)
    return sum(test_values_passed)


print(f"Part 1 result: {get_result()}")
print(f"Part 2 result: {get_result(part=2)}")
