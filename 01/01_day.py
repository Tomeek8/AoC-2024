with open("input.txt") as f:
    lines = f.read().splitlines()

column_1 = sorted((int(x.split()[0]) for x in lines))
column_2 = sorted((int(x.split()[1]) for x in lines))

result_1 = sum(abs(x - y) for x, y in zip(column_1, column_2))
print(result_1)


result_2 = sum(num * column_2.count(num) for num in column_1)
print(result_2)
