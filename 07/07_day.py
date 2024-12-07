import time


def parse(path):
    with open(path) as f:
        return [
            (
                int(line.split(": ")[0]),
                list(map(int, (line.split(": ")[1].strip().split(" ")))),
            )
            for line in f.read().splitlines()
        ]


def is_equation_valid(test_value, numbers, part):
    partial_sums = [numbers[0]]
    for num in numbers[1:]:
        new_partial_sums = []
        for partial_sum in partial_sums:
            if (np1 := partial_sum + num) <= test_value:
                new_partial_sums.append(np1)
            if (np2 := partial_sum * num) <= test_value:
                new_partial_sums.append(np2)
            if part == 2:
                if (np3 := int(f"{partial_sum}{num}")) <= test_value:
                    new_partial_sums.append(np3)
        partial_sums = new_partial_sums
    return test_value in partial_sums


def get_result():
    data = parse("./07/input.txt")
    test_values_passed1 = []
    test_values_passed2 = []
    for test_value, numbers in data:
        if is_equation_valid(test_value, numbers, part=1):
            test_values_passed1.append(test_value)
        elif is_equation_valid(test_value, numbers, part=2):
            test_values_passed2.append(test_value)           
    return sum(test_values_passed1), sum(test_values_passed2)


start_time = time.time()

result1, result2 = get_result()
print(f"Part 1 result: {result1}")
print(f"Part 2 result: {result2}")

print(f"Time: {time.time() - start_time:.3f} s")
# Time: 1.627 s
