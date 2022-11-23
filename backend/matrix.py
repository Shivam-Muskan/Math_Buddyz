import numpy as np

num = int(input("Total no. of matrices: "))
matrices = {}


def print_matrix(M, rowSize, colSize):
    for row_id in range(rowSize):
        for col in range(colSize):
            print(M[row_id][col], end=" ")
        print()


def matrix_multiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
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
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                result[i][j] += A[i][j] + B[i][j]
    else:
        print("Addition Not possible because of invalid matrix size.")

    print("The resultant Matrix after Addition : ", result)
    return result


def matrix_det(A):
    determinant = np.linalg.det(A)
    print("The determinant of the matrix is : ",determinant)
    return determinant


def matrix_transpose(A):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[j][i]
    print("The transpose of matrix is : ",result)
    print_matrix(result,len(result),len(result[0]))
    return result


def matrix_inverse(A):
    determinant = np.linalg.det(A)
    if determinant != 0 :
        inverse = np.linalg.inv(A)
        print("The inverse Matrix is :\n", inverse)
        return inverse
    else:
        print("Singular matrix. Inverse cannot be found.")
        return 0


for i in range(num):
    rows = int(input(f"No. of rows for Matrix {i + 1} : "))
    cols = int(input(f"No. of columns in Matrix {i + 1} : "))

    matrices[i] = [[0 for _ in range(cols)] for _ in range(rows)]
    print(matrices[i])
    print(f"Enter the elements of Matrix {i} : ")
    for k in range(rows):
        row = input('Enter a row: ')
        if len(row.split(sep=',')) == int(cols):
            matrices[i][k] = [int(x) for x in row.split(",")]
        else:
            print("Invalid!")
            row = input('Enter a row: ')
            if len(row.split(sep=',')) == cols:
                matrices[i][k] = [int(x) for x in row.split(",")]
                break
    print(matrices[i])
    print_matrix(matrices[i], rows, cols)
    matrix_det(matrices[i])
    matrix_transpose(matrices[i])
    matrix_inverse(matrices[i])

matrix_result = []
resultant = matrix_multiplication(matrices[0], matrices[1])
matrix_result.append(resultant)
for n in range(2, num):
    resultant = matrix_multiplication(matrix_result[n - 2], matrices[n])
    matrix_result.append(resultant)

matrix_result1 = []
resultant1 = matrix_add(matrices[0], matrices[1])
matrix_result1.append(resultant)
for n in range(2, num):
    resultant = matrix_add(matrix_result1[n - 2], matrices[n])
    matrix_result1.append(resultant)
