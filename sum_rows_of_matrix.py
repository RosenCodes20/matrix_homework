n = int(input())

matrix = []
count = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    matrix.append(row)

print("\n".join(map(str, [sum(elements) for elements in matrix])))
