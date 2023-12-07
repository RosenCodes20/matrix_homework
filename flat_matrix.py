n = int(input())

matrix = []
count = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    matrix.append(row)
new_matrix = []
for row in matrix:
    for element in row:
        new_matrix.append(element)

print(new_matrix)

