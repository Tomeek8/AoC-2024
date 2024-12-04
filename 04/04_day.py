import collections

with open("./04/input.txt") as f:
    matrix = f.read().splitlines()

WORD = "XMAS"


def check_index(x):
    if x < 0:
        raise IndexError


def find_xmas_around(x, y, word, matrix):
    word_length = len(word)
    xmas_count = 0
    # horizonatal right
    for i in range(word_length):
        try:
            if matrix[x][y + i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # diagonal down right
    for i in range(word_length):
        try:
            if matrix[x + i][y + i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # vertical down
    for i in range(word_length):
        try:
            if matrix[x + i][y] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # diagonal down left
    for i in range(word_length):
        try:
            check_index(y - i)
            if matrix[x + i][y - i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # horizonatal left
    for i in range(word_length):
        try:
            check_index(y - i)
            if matrix[x][y - i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # diagonal up left
    for i in range(word_length):
        try:
            check_index(x - i)
            check_index(y - i)
            if matrix[x - i][y - i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # vertical up
    for i in range(word_length):
        try:
            check_index(x - i)
            if matrix[x - i][y] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1

    # diagonal up right
    for i in range(word_length):
        try:
            check_index(x - i)
            if matrix[x - i][y + i] != word[i]:
                break
        except IndexError:
            break
    else:
        xmas_count += 1
    return xmas_count


def sum_matrix_xmas(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    xmas_total = 0
    for row_i in range(rows_count):
        for column_i in range(columns_count):
            xmas_total += find_xmas_around(row_i, column_i, "XMAS", matrix)
    return xmas_total


# PART 2
def find_X_MAS(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    xmas_total = 0
    for row_i in range(1, rows_count - 1):
        for column_i in range(1, columns_count - 1):
            if matrix[row_i][column_i] != "A":
                continue
            diagonal1 = []
            diagonal1 += matrix[row_i + 1][column_i + 1]
            diagonal1 += matrix[row_i - 1][column_i - 1]
            diagonal2 = []
            diagonal2 += matrix[row_i + 1][column_i - 1]
            diagonal2 += matrix[row_i - 1][column_i + 1]
            if sorted(diagonal1) == sorted(diagonal2) == ["M", "S"]:
                xmas_total += 1
    return xmas_total


print(f"Part 1 result: {sum_matrix_xmas(matrix)}")
print(f"Part 2 result: {find_X_MAS(matrix)}")
