import math


# Умножение матрицы на число
def number_on_matrix(number, matrix):
    new_matrix = []

    for i in range(0, len(matrix)):
        new_matrix.append(list(matrix[i]))
        for j in range(0, len(matrix[i])):
            new_matrix[i][j] = number * matrix[i][j]

    return new_matrix


# Умножение вектора на число
def number_on_vector(number, vector):
    new_vector = []

    for i in range(0, len(vector)):
        new_vector.append(list(vector))
        new_vector[i] = number * vector[i]

    return new_vector


# Умножение матрицы на матрицу
def matrix_on_matrix(a, b):
    sum_mult = 0
    new_matrix = []

    for i in range(0, len(a)):
        new_matrix.append(list(a[i]))
        for j in range(0, len(a[i])):
            for k in range(0, len(a)):
                sum_mult += a[i][k] * b[k][j]
            new_matrix[i][j] = sum_mult
            sum_mult = 0

    return new_matrix


# Умножение матрицы на матрицу
def matrix_on_vector(a, b):
    sum_mult = 0
    new_vector = []

    for i in range(0, len(a)):
        new_vector.append(list(b))
        for j in range(0, len(a[i])):
            sum_mult += a[i][j] * b[j]
        new_vector[i] = sum_mult
        sum_mult = 0

    return new_vector


# Вычитание матриц
def matrix_minus_matrix(a, b):
    new_matrix = []

    for i in range(0, len(a)):
        new_matrix.append(list(a[i]))
        for j in range(0, len(a[i])):
            new_matrix[i][j] = a[i][j] - b[i][j]

    return new_matrix


# Сложение матриц
def matrix_plus_matrix(a, b):
    new_matrix = []

    for i in range(0, len(a)):
        new_matrix.append(list(b[i]))
        for j in range(0, len(a[i])):
            new_matrix[i][j] = a[i][j] + b[i][j]

    return new_matrix


# Сложение вектора и матрицы
def vector_plus_vector(a, b):
    new_vector = []

    for i in range(0, len(a)):
        new_vector.append(list(a))
        new_vector[i] = a[i] + b[i]

    return new_vector


# Нормирование вектора
def normalize(x):
    length = 0

    for i in range(0, len(x)):
        length += x[i] ** 2
    length = math.sqrt(length)

    for i in range(0, len(x)):
        x[i] = x[i] / length
    return x
