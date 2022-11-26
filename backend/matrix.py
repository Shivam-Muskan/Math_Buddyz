from typing import List

import numpy as np


def initialize():
    no_of_matrices = int(input("Total no. of matrices: "))
    all_matrices = {}

    for i in range(no_of_matrices):
        rows = int(input(f"No. of rows for Matrix {i + 1} : "))
        cols = int(input(f"No. of columns in Matrix {i + 1} : "))

        all_matrices[i] = [[0 for _ in range(cols)] for _ in range(rows)]
        print(f"Enter the elements of Matrix {i} : ")
        for k in range(rows):
            row = input('Enter a row: ')
            if len(row.split(sep=',')) == cols:
                all_matrices[i][k] = [int(x) for x in row.split(",")]
            else:
                print("Invalid!")
                row = input('Enter a row: ')
                if len(row.split(sep=',')) == cols:
                    all_matrices[i][k] = [int(x) for x in row.split(",")]
                    break
        print_matrix(all_matrices[i], rows, cols)
        matrix_det(all_matrices[i])
        matrix_transpose(all_matrices[i])
        matrix_inverse(all_matrices[i])

    return all_matrices, no_of_matrices


def print_matrix(M, rowSize, colSize):
    for row_id in range(rowSize):
        for col in range(colSize):
            print(M[row_id][col], end=" ")
        print()


def matrix_multiplication(A: List, B: List):
    # result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    result = [[0] * len(B[0])] * len(A)  # Easy way to create 0 filled Array
    if len(A[0]) == len(B):
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
    else:
        print("Multiplication Not possible because of invalid matrix size.")

    print("The resultant Matrix after Multiplication : ", result)
    return result


def matrix_add(A, B):
    # result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    result = [[0] * len(B[0])] * len(A)  # Easy way to create 0 filled Array
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] += A[i][j] + B[i][j]
        print("The resultant Matrix after Addition : ", result)

    else:
        print("Addition Not possible because of invalid matrix size.")

    return result


def matrix_det(A):
    if len(A) == len(A[0]):
        determinant = np.linalg.det(A)
        print("The determinant of the matrix is : ", determinant)
        return determinant


def matrix_transpose(A):
    # result = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    result = [[0] * len(A)] * len(A[0])  # Easy way to create 0 filled Array
    print(result)
    for i in range(len(A[0])):
        for j in range(len(A)):
            result[i][j] = A[j][i]
    print("The transpose of matrix is : ", result)
    print_matrix(result, len(result), len(result[0]))
    return result


def matrix_inverse(A):
    if len(A) == len(A[0]):
        determinant = np.linalg.det(A)
        if determinant != 0:
            inverse = np.linalg.inv(A)
            print("The inverse Matrix is :\n", inverse)
            return inverse
        else:
            print("Singular matrix. Inverse cannot be found.")
            return 0


def multiple_matrix_multiply(all_matrices, total_matrices):
    resultant = matrix_multiplication(all_matrices[0], all_matrices[1])
    matrix_result = [resultant]
    if total_matrices > 2:
        for matrix_index in range(2, total_matrices):
            resultant = matrix_multiplication(matrix_result[matrix_index - 2], all_matrices[matrix_index])
            matrix_result.append(resultant)
    return matrix_result[-1]


def multiple_matrix_addition(all_matrices, total_matrices):
    addition_resultant = matrix_add(all_matrices[0], all_matrices[1])
    matrix_result1 = [addition_resultant]
    if total_matrices > 2:
        for matrix_index in range(2, total_matrices):
            resultant = matrix_add(matrix_result1[matrix_index - 2], all_matrices[matrix_index])
            matrix_result1.append(resultant)
    return matrix_result1[- 1]


if __name__ == '__main__':
    matrices, num = initialize()
    multiply_result = multiple_matrix_multiply(matrices, num)
    addition_result = multiple_matrix_addition(matrices, num)

    print("Multiplication: ", '\n', print_matrix(multiply_result, len(multiply_result), len(multiply_result[0])))
    print("Addition: ", '\n', print_matrix(addition_result, len(addition_result), len(addition_result[0])))
