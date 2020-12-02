import numpy as np
from matrix_operations import *


def get_p(n, matrix):
    sum_diagonal = 0

    for i in range(0, len(matrix)):
        sum_diagonal += matrix[i][i]

    return 1 / n * sum_diagonal


def get_b(a, p, e):
    return matrix_minus_matrix(a, number_on_matrix(p, e))


def get_a(a, b):
    return matrix_on_matrix(a, b)


def get_y(eigenvalue, y, b):
    return vector_plus_vector(number_on_vector(eigenvalue, y), b)


# Проверка реузльтат
def check_result(a, x, eigenvalue):
    print(matrix_on_vector(a, x))
    print(number_on_vector(eigenvalue, x))


# Исходная матрица
A = [[18, 1, 8, 1],
     [1, 10, 1, 0],
     [8, 1, -84, 1],
     [1, 0, 1, 20.33445375]]

# Единичная матрица
E = [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

list_p = []
list_B = []
list_A = [A]


def main():
    # Поиск коэфициентов характеристического уравнения
    for n in range(0, len(A)):
        list_p.append(get_p(n + 1, list_A[n]))
        list_B.append(get_b(list_A[n], list_p[n], E))
        list_A.append(get_a(A, list_B[n]))

    print("Характеристическое уравнение матрицы A имеет вид:")
    print(f"\u03BB^4 - {list_p[0]}\u03BB^3 - {list_p[1]}\u03BB^2 - {list_p[2]}\u03BB - {list_p[3]} = 0\n")

    # Нахождение собственных значений матрицы(корней уравнения)
    eigenvalues = -np.roots([-1, -list_p[0], list_p[1], -list_p[2], list_p[3]])

    eigenvalues = list(eigenvalues)

    for i in range(0, len(eigenvalues)):
        eigenvalues[i] = float(eigenvalues[i])

    print("Собственные значения матрицы A:", eigenvalues, "", sep='\n')

    x = []
    # Первые столбцы найденых выше матриц
    y0 = E[0]
    b1 = list_B[0][0]
    b2 = list_B[1][0]
    b3 = list_B[2][0]

    # Нахождение собственных векторов
    for k in range(0, len(A)):
        y1 = get_y(eigenvalues[k], y0, b1)
        y2 = get_y(eigenvalues[k], y1, b2)
        x.append(get_y(eigenvalues[k], y2, b3))

    print("Собственные вектора матрицы A:")
    for i in range(0, len(x)):
        print(x[i])

    print("\nНормализованные вектора матрицы A:")
    for i in range(0, len(x)):
        normalize(x[i])
        print(x[i])

    print("\nПроверка:")
    for i in range(0, len(x)):
        print(f"{i + 1})")
        check_result(A, x[i], eigenvalues[i])


if __name__ == '__main__':
    main()
