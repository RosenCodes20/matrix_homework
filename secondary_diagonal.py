n = int(input())
matrix = []
for i in range(n):
    rows = list(map(int, input().split(", ")))
    matrix.append(rows)

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][n - i - 1]
print(diagonal_sum)
