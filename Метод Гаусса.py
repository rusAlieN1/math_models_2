print('Введите количество переменных:')
n = int(input())

matrix = []

print("Введите коэффициенты:")

for i in range(n):
    a = []
    for j in range(n + 1):
        a.append(int(input()))
    matrix.append(a)

for i in range(n):
    for j in range(n + 1):
        print(matrix[i][j], end=" ")
    print()

print()
for k in range(n):
    normal = matrix[k][k]
    for i in range(0, n):
        kof = matrix[i][k]
        if i != k:
            for j in range(n + 1):
                matrix[i][j] = matrix[i][j] - (matrix[k][j] * kof / normal)

for i in range(n):
    for j in range(n + 1):
        print(matrix[i][j], end=" ")
    print()

print()
for x in range(n):
    x0 = x + 1
    x = matrix[x][n] / matrix[x][x]
    print("Значение переменной x_" + str(x0) + ":", x)
