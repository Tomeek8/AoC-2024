import time


def parse(path):
    with open(path) as f:
        return f.read().strip()


def fragment_data_1(line):
    fragmented = []
    for i, num in enumerate(line):
        if i % 2 == 0:
            fragmented.extend([(i // 2)] * int(num))
        else:
            fragmented.extend(["."] * int(num))
    return fragmented


def defragment_1(data):
    last_index = len(data) - 1
    for i in range(len(data)):
        if data[i] == ".":
            while last_index >= 0 and data[last_index] == ".":
                last_index -= 1
            if last_index > i:
                data[i] = data[last_index]
                data[last_index] = "."
                last_index -= 1
    no_dots = [x for x in data if x != "."]
    # print(no_dots)
    return no_dots


def find_free_space(data, size):
    for i in range(len(data)):
        if data[i : i + size] == ["."] * size:
            return i


def get_last_file(data):
    f = []
    index = len(data)
    for i in range(len(data) - 1, 0, -1):
        if data[i] == ".":
            continue
        if f == [] or data[i] in f:
            f.append(data[i])
            index = i
        else:
            break
    return f, index


def defragment_2(data):
    index = len(data)
    while index > 1:
        last_file, lf_i = get_last_file(data[:index])
        fs_index = find_free_space(data[:index], len(last_file))
        if fs_index:
            data[fs_index : fs_index + len(last_file)] = last_file
            data[lf_i : lf_i + len(last_file)] = ["."] * len(last_file)
        index = lf_i
        # print(data)
    return data


def final_sum(data):
    total = 0
    for i, num in enumerate(data):
        if isinstance(num, int):
            total += i * num
    # print(total)
    return total


def part1(data):
    fd = fragment_data_1(data)
    dd = defragment_1(fd)
    return final_sum(dd)


def part2(data):
    fd = fragment_data_1(data)
    dd2 = defragment_2(fd)
    return final_sum(dd2)


start_time = time.time()
data = parse("09/input.txt")

print(f"Part 1 result: {part1(data)}")
print(f"Part 2 result: {part2(data)}")
print(f"Time: {time.time() - start_time:.3f} s")

# Part 1 result: 6291146824486
# Part 2 result: 6307279963620
# Time: 136.632 s
