import math as m
import random
import numpy as np
import copy


def roots():
    a, b, c = [int(x) for x in input("Insert a,b,c: ").split()]
    delta = ((b**2) - (4*a*c))
    x = []
    if delta > 0:
        x.append((-b + m.sqrt(delta)) / (2*a))
        x.append((-b - m.sqrt(delta)) / (2*a))
    elif delta == 0:
        x.append(-b / (2*a))
    else:
        x.append("no roots")
    print(x)


def sort():
    sort_numbers = []
    numbers = [random.randint(0, 100) for x in range(100)]
    for i in range(len(numbers)):
        flag = False
        if (i == 0):
            sort_numbers.append(numbers[i])
        else:
            for j in range(len(sort_numbers)):
                if numbers[i] > sort_numbers[j]:
                    sort_numbers.insert(j, numbers[i])
                    flag = True
                    break
            if flag == False:
                sort_numbers.append(numbers[i])
    print(numbers)
    numbers.sort(reverse=True)
    print(numbers)
    print(sort_numbers)
  

def scalar():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    product = sum([a[x] * b[x] for x in range(len(a))])
    print(product)


def matrix_sum():
    mat1 = [([random.randint(0, 100) for i in range(128)]) for j in range(128)]
    mat2 = [([random.randint(0, 100) for i in range(128)]) for j in range(128)]
    res = [([mat1[i][j] + mat2[i][j] for i in range(128)]) for j in range(128)]


def matrix_multiply():
    mat1 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    mat2 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    res = [([0 for i in range(8)]) for j in range(8)]
    print(mat1)
    print(mat2)
    for i in range(8):
        for j in range(8):
            for k in range(8):
                res[i][j] += mat1[i][k] + mat2[j][k]
    print(res)

def get_minor_matrix(matrix, row, col):
    minor_matrix = copy.deepcopy(matrix)
    minor_matrix.pop(row)
    for i in range(len(minor_matrix)):
        minor_matrix[i].pop(col)
    return minor_matrix


def calc_determinant_of_matrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for i in range(len(matrix)):
        determinant += matrix[0][i] * calc_determinant_of_matrix(
            get_minor_matrix(matrix, 0, i)) * (-1) ** i
    return determinant    


if __name__ == '__main__':
    #roots()
    #sort()
    #scalar()
    #matrix_sum()
    #matrix_multiply()

    #matrix det
    dim_of_matrix = 5
    A = [[random.random() for _ in range(dim_of_matrix)]
         for _ in range(dim_of_matrix)]
    if (np.allclose(calc_determinant_of_matrix(A), np.linalg.det(A))):
        print("ok")
    else:
        print("not ok")
    
