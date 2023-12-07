n = int(input())
matrix = []
for i in range(n):
    rows = list(map(int, input().split(", ")))
    matrix.append(rows)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)