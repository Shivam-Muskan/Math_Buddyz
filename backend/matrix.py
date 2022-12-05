def initialize():
    no_of_matrices = int(input("Total no. of matrices: "))
    all_matrices = {}

    for i in range(no_of_matrices):
        print('')
        rows = int(input(f"No. of rows for Matrix {i + 1} : "))
        cols = int(input(f"No. of columns in Matrix {i + 1} : "))

        all_matrices[i] = [[0 for _ in range(cols)] for _ in range(rows)]
        print(all_matrices[i],'\n')
        print(f"Enter the elements of Matrix {i+1} : ")
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
        print('\n',"Determinant :")
        print("The determinant of the matrix is : ", matrix_det(all_matrices[i]))
        print('\n',"Transpose :")
        matrix_transpose(all_matrices[i])
        print('\n',"Inverse :",'\n')
        matrix_inverse(all_matrices[i])

    return all_matrices, no_of_matrices


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
        print("The resultant Matrix after Addition : ", result)

    else:
        print("Addition Not possible because of invalid matrix size.")

    return result


def matrix_minor(A, i, j):
    return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]


def matrix_det(A):
    if len(A) == len(A[0]):
        if len(A) == 2:
            determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]
            return determinant

        determinant = 0
        for c in range(len(A)):
            determinant += ((-1) ** c) * A[0][c] * matrix_det(matrix_minor(A, 0, c))

        return determinant

    else:
        print("Not a square matrix. Determinant cannot be determined.")
        return 0


def matrix_transpose(A):
    result = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            result[i][j] = A[j][i]

    print("The transpose of matrix is : ", result)
    print_matrix(result, len(result), len(result[0]))
    return result


def matrix_cofactor(A):
    cofactors = []
    for r in range(len(A)):
        cofactorRow = []
        for c in range(len(A)):
            minor = matrix_minor(A, r, c)
            cofactorRow.append(((-1) ** (r + c)) * matrix_det(minor))
        cofactors.append(cofactorRow)

    print("CoFactors : ",cofactors)
    print_matrix(cofactors, len(cofactors), len(cofactors[0]))
    return cofactors


def matrix_adjoint(A):
    cofactors = matrix_cofactor(A)
    adjoint = matrix_transpose(cofactors)
    return adjoint


def matrix_inverse(A):
    determinant = matrix_det(A)

    if len(A) == 2:
        inverse = [[A[1][1] / determinant, -1 * A[0][1] / determinant],
                [-1 * A[1][0] / determinant, A[0][0] / determinant]]
        print("The inverse Matrix is :\n", inverse)
        print_matrix(inverse, len(inverse), len(inverse[0]))
        return inverse

    inverse = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    if determinant != 0 :
        adjoint = matrix_adjoint(A)
        for r in range(len(adjoint)):
            for c in range(len(adjoint)):
                inverse[r][c] = adjoint[r][c] / determinant

        print("The inverse Matrix is :\n", inverse)
        print_matrix(inverse, len(inverse), len(inverse[0]))
        return inverse
    else:
        print("Singular matrix. Inverse cannot be found.")
        return


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

    print('\n',"Multiplication :")
    multiply_result = multiple_matrix_multiply(matrices, num)
    print_matrix(multiply_result, len(multiply_result), len(multiply_result[0]))

    print('\n',"Addition :")
    addition_result = multiple_matrix_addition(matrices, num)
    print_matrix(addition_result, len(addition_result), len(addition_result[0]))
