from sympy import diff, symbols, sin, cos

x, y = symbols('x y')
matrix = []
print("Введите координату точки отсчёта x:")
x0 = float(input())
print("Введите координату точки отсчёта y:")
y0 = float(input())
print("Введите погрешность:")
fault = float(input())
n = 2
iter_count = 0


def f1(x, y):
    return sin(y) + 2 * x - 2


def f2(x, y):
    return cos(x - 1) + y - 0.7


def dx1(x, y):
    return 2


def dy1(x, y):
    return cos(y)


def dx2(x, y):
    return -1 * sin(x - 1)


def dy2(x, y):
    return 1


x_prev = 0
y_prev = 0
x = x0
y = y0

while abs(x - x_prev) >= fault and abs(y - y_prev) >= fault:
    for i in range(0, 1):
        a = []
        for j in range(n + 1):
            a.append(dx1(x, y))
            a.append(dy1(x, y))
            a.append(-1 * f1(x, y))
        matrix.append(a)
    for i in range(1, n):
        a = []
        for j in range(n + 1):
            a.append(dx2(x, y))
            a.append(dy2(x, y))
            a.append(-1 * f2(x, y))
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
    h = matrix[0][2] / matrix[0][0]
    print("h" + ":", h)
    k = matrix[1][2] / matrix[1][1]
    print("k" + ":", k)
    matrix = []
    x_prev = x
    y_prev = y
    x = x + h
    y = y + k
    print()
    print()
    iter_count += 1

print("Значение переменной x_" + ":", x)
print("Значение переменной y_" + ":", y)
print("Количество итераций:", iter_count)
