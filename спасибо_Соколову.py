import numpy as np
from numpy import linalg
from TableDraw import Table


def create_matrix():
    try:
        n = int(input('Введите размерность квадратной матрицы: '))
    except ValueError:
        print('Нужно было ввести число!')
        exit()

    matrix = np.zeros((n, n))

    try:
        for i in range(n):
            for j in range(n):
                matrix[i, j] = float(input(f'Введите {i}, {j} элемент матрицы: '))
    except ValueError:
        print('Нужно было вводить числа!')
        exit()

    return matrix


def test_matrix(matrix):
    diagonal = matrix.diagonal()
    check = False if 0 in diagonal else True

    if not check:
        print('\nДиагональ матрицы содержит нулевые элементы!\nПрограмма завершена.')
        exit()


def main_calculation(a):
    n = len(a)
    L = np.ones((n, n))
    U = np.ones((n, n))

    for j in range(n):
        U[0, j] = a[0, j]

    for j in range(1, n):
        L[j, 0] = a[j, 0] / U[0, 0]

    for i in range(1, n):
        for j in range(i, n):
            U[i, j] = a[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

    for i in range(1, n):
        for j in range(i + 1, n):
            L[j, i] = 1 / U[i, i] * (a[j, i] - sum(L[j, k] * U[k, i] for k in range(i)))

    for i in range(n):
        for j in range(n):
            if i > j:
                U[i, j] = 0
            if i < j:
                L[i, j] = 0

    P = L * U

    print_matrix(L, 'Треугольная L-матрица')
    print_matrix(U, 'Треугольная U-матрица')
    print_matrix(P, 'L*U-матрица')

    b = np.eye(n, dtype=float)
    y = np.zeros((n, n))
    x = np.zeros((n, n))

    for i, elem in enumerate(b):
        transpose_elem = np.transpose(elem)
        y[i] = linalg.solve(L, transpose_elem)
        x[i] = linalg.solve(U, y[i])

    print_matrix(np.transpose(x), 'Обратная матрица')


def print_matrix(matrix, name):
    n = [str(i) for i in range(len(matrix))]
    table = Table(name, n)

    for elem in matrix:
        table.insert_row([str(i) for i in elem])

    line = '=' * 5 + '=' * len(matrix) * 6
    print('\n' + line)
    table.print_table(enum=True)
    print(line)