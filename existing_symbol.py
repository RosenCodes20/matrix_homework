n = int(input())
matrix = []
for i in range(n):
    symbols = input()
    matrix.append(list(symbols))

element_to_found = input()
found = False
for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j] == element_to_found:
            print(f"({i}, {j})")
            found = True
            break
if not found:
    print(f"{element_to_found} not in our matrix!")