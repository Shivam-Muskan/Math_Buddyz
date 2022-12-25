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
        '''print('\n',"Determinant :")
        print("The determinant of the matrix is : ", matrix_det(all_matrices[i]))
        print('\n',"Transpose :")
        matrix_transpose(all_matrices[i])
        print('\n',"Inverse :",'\n')
        inverse = matrix_inverse(all_matrices[i])
        print_matrix(inverse, len(inverse), len(inverse[0]))'''

        print('\n',"Trace :",'\n')
        matrix_trace(all_matrices[i])

        print('\n', "Matrix power n : ")
        n = int(input("Enter the power : "))
        exponent_result = matrix_power_n(all_matrices[i], n)
        if exponent_result is not None:
            print_matrix(exponent_result, len(exponent_result), len(exponent_result[0]))

    return all_matrices, no_of_matrices


def print_matrix(matrix, rowSize, colSize):
    for row_id in range(rowSize):
        for col in range(colSize):
            print(matrix[row_id][col], end=" ")
        print()


def matrix_multiplication(matrix_1, matrix_2):
    if len(matrix_1[0]) == len(matrix_2):
        result = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
        print("The resultant Matrix after Multiplication : ", result)
        return result

    print("Multiplication Not possible because of invalid matrix size.")
    return None


def matrix_add(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2) == len(matrix_1[0]) == len(matrix_2[0]):
        result = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                result[i][j] += matrix_1[i][j] + matrix_2[i][j]
        print("The resultant Matrix after Addition : ", result)
        return result

    print("Addition Not possible because of invalid matrix size.")
    return None


def matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i + 1:])]


def matrix_det(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 2:
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return determinant

        determinant = 0
        for c in range(len(matrix)):
            determinant += ((-1) ** c) * matrix[0][c] * matrix_det(matrix_minor(matrix, 0, c))

        return determinant

    print("Not a square matrix. Determinant cannot be determined.")
    return None


def matrix_transpose(matrix):
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    print("The transpose of matrix is : ", result)
    print_matrix(result, len(result), len(result[0]))
    return result


def matrix_cofactor(matrix):
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = matrix_minor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * matrix_det(minor))
        cofactors.append(cofactorRow)

    print("CoFactors : ",cofactors)
    print_matrix(cofactors, len(cofactors), len(cofactors[0]))
    return cofactors


def matrix_adjoint(matrix):
    if len(matrix) == 2:
        adjoint = [[matrix[1][1] , -1 * matrix[0][1]],
                   [-1 * matrix[1][0] , matrix[0][0]]]
        print("The adjoint of Matrix is :\n", adjoint)
        return adjoint

    cofactors = matrix_cofactor(matrix)
    adjoint = matrix_transpose(cofactors)
    return adjoint


def matrix_inverse(matrix):
    if len(matrix) != len(matrix[0]):
        print("Not a square matrix. Inverse cannot be found.")
        return None, None, "Not a square matrix. Inverse cannot be found."

    determinant = matrix_det(matrix)

    if determinant == 0:
        print("Singular matrix. Inverse cannot be found.")
        return None, None, "Singular matrix. Inverse cannot be found."

    if len(matrix) == 2:
        inverse = [[round(matrix[1][1] / determinant, 2), round(-1 * matrix[0][1] / determinant, 2)],
                   [round(-1 * matrix[1][0] / determinant, 2), round(matrix[0][0] / determinant,2)]]
        print("The inverse Matrix is :\n", inverse)
        return inverse, determinant, None

    if determinant != 0:
        inverse = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        adjoint = matrix_adjoint(matrix)
        for r in range(len(adjoint)):
            for c in range(len(adjoint)):
                inverse[r][c] = round(adjoint[r][c] / determinant, 2)

        print("The inverse Matrix is :\n", inverse)
        return inverse, determinant, None

    print("Inverse cannot be found.")
    return None, None, "Inverse cannot be found."


def multiple_matrix_multiply(all_matrices, total_matrices):
    resultant = matrix_multiplication(all_matrices[0], all_matrices[1])
    if resultant is None:
        return None

    matrix_result = [resultant]
    if total_matrices > 2:
        for matrix_index in range(2, total_matrices):
            resultant = matrix_multiplication(matrix_result[matrix_index - 2], all_matrices[matrix_index])
            if resultant is None:
                return None
            matrix_result.append(resultant)
    return matrix_result[-1]


def multiple_matrix_addition(all_matrices, total_matrices):
    addition_resultant = matrix_add(all_matrices[0], all_matrices[1])
    if addition_resultant is None:
        return None

    matrix_result1 = [addition_resultant]
    if total_matrices > 2:
        for matrix_index in range(2, total_matrices):
            resultant = matrix_add(matrix_result1[matrix_index - 2], all_matrices[matrix_index])
            if resultant is None:
                return None
            matrix_result1.append(resultant)
    return matrix_result1[- 1]


def matrix_trace(matrix):
    if len(matrix) != len(matrix[0]):
        print("Not a square matrix. Trace cannot be found.")
        return None

    trace = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if i == j :
                trace += matrix[i][j]

    print("Trace of given matrix is :", trace)
    return trace


def matrix_power_n(matrix, n):
    if len(matrix) != len(matrix[0]):
        print("Not a square matrix.")
        return None, "Not a square matrix."

    if n == 0:
        print("Matrix power cannot be zero.")
        return None, "Matrix power cannot be zero."

    if n < 0 and matrix_det(matrix) == 0:
        print("Power should be positive for singular matrix.")
        return None, "Power should be positive for singular matrix."

    if n < 0 and matrix_det(matrix) != 0:
        n = -n
        power_matrices = []
        for i in range(n):
            power_matrices.append(matrix)

        res = multiple_matrix_multiply(power_matrices, n)
        result = matrix_inverse(res)
        return result, None

    power_matrices = []
    for i in range(n):
        power_matrices.append(matrix)

    result = multiple_matrix_multiply(power_matrices, n)

    return result, None


if __name__ == '__main__':
    matrices, num = initialize()

    '''print('\n',"Multiplication :")
    multiply_result = multiple_matrix_multiply(matrices, num)
    print_matrix(multiply_result, len(multiply_result), len(multiply_result[0]))

    print('\n',"Addition :")
    addition_result = multiple_matrix_addition(matrices, num)
    print_matrix(addition_result, len(addition_result), len(addition_result[0]))'''


'''
# Another Method :
def matrix_power(matrix, power):
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    determinant = matrix_det(matrix)
    print("det:", determinant)
    trace = matrix_trace(matrix)

    if determinant == 0 and len(matrix) == 2:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                result[i][j] = (trace ** (power - 1)) * matrix[i][j]

        return result

    if determinant != 0 and len(matrix) == 2 and power == 2:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if i == j:
                    result[i][j] = (trace ** (power - 1)) * matrix[i][j] - determinant

                result[i][j] = (trace ** (power - 1)) * matrix[i][j]

        return result
'''


