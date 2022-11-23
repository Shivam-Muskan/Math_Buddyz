num = int(input("Total no. of matrices: "))
matrices = {}


def print_matrix(M, rowSize, colSize):
    for row_id in range(rowSize):
        for col in range(colSize):
            print(M[row_id][col], end=" ")
        print()
    return 'Done'


results = [[]]
results_row = 0
results_col = 0


def matrix_multiplication(A, B, rowA, rowB, colA, colB):
    result = [[0 for _ in range(rowA)] for _ in range(colB)]
    if colA == rowB:
        for i in range(rowA):
            for j in range(colB):
                for k in range(rowB):
                    result[i][j] += A[i][k] * B[k][j]

    else:
        print("Invalid!")

    print("Resultant Matrix : ", result)
    print_matrix(result, rowA, colB)

    results.append(result)
    results_row = rowA
    results_col = colB
    print(results_row, results_col)


total_rows = []
total_cols = []
for i in range(num):
    rows = int(input(f"No. of rows for Matrix {i + 1} : "))
    cols = int(input(f"No. of columns in Matrix {i + 1} : "))
    total_rows.append(rows)
    total_cols.append(cols)

    matrices[i] = [[0 for _ in range(cols)] for _ in range(rows)]
    print(matrices[i])
    print(f"Enter the elements of Matrix {i} : ")
    for k in range(rows):
        row = input('Enter a row: ')
        if len(row.split(sep=',')) == cols:
            matrices[i][k] = [int(x) for x in row.split(",")]
        else:
            print("Invalid!")
            row = input('Enter a row: ')
            if len(row.split(sep=',')) == cols:
                matrices[i][k] = [int(x) for x in row.split(",")]
                break
    print(matrices[i])
    print_matrix(matrices[i], rows, cols)


# matrix_multiplication(matrices[0], matrices[1], total_rows[0], total_rows[1], total_cols[0], total_cols[1])

# for n in range(2, num):
#     matrix_multiplication(results[n-2], matrices[n], results_row, total_rows[n], results_col, total_cols[n])


def matrix_mul(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
    print("Multiplication Not possible because of matrix size")
    return 0


def multiple_matrix_multiplication(matrix: {}) -> str or []:
    result = matrix_mul(matrix[0], matrix[1])
    if result == 0:
        return 'Multiplication Not possible because of matrix size'
    result_matrices = [result]

    if len(matrix) < 2:
        return result_matrices

    for n in range(2, len(matrix)):
        result = matrix_mul(result_matrices[n - 2], matrix[n])
        if result == 0:
            return 'Multiplication Not possible because of matrix size'
        result_matrices.append(result)

    return result_matrices[-1]


final_result = multiple_matrix_multiplication(matrices)

if type(final_result) is str:
    print(final_result)
else:
    print("Resultant Matrix", print_matrix(final_result, len(final_result), len(final_result[0])))
