def initialize():
    order = int(input("Order of Matrix : "))

    mat = [[0 for _ in range(order)] for _ in range(order)]
    print(mat, '\n')

    print("Enter the elements of Matrix : ")

    for i in range(order):
        row = input(f'Enter row {i+1}: ')

        if len(row.split(sep=',')) == order:
            mat[i] = [int(x) for x in row.split(",")]
        else:
            print("Invalid row!")

    print_matrix(mat)
    return mat


def print_matrix(mat):
    for row_id in range(len(mat)):
        for col_id in range(len(mat)):
            print(mat[row_id][col_id], end=" ")
        print()


def is_upper_triangular(mat):
    for i in range(1, len(mat)):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True


def is_lower_triangular(mat):
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            if mat[i][j] != 0:
                return False
    return True


def is_square(mat):
    if len(mat) != len(mat[0]):
        return False
    return True


def is_diagonal(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0 :
                return False
    return True


def is_scaler(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0 :
                return False

    for i in range(len(mat) - 1):
        if mat[i][i] != mat[i + 1][i + 1]:
            return False

    return True


def is_identity(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0:
                return False

    for i in range(len(mat)):
        if mat[i][i] != 1:
            return False

    return True


def is_null(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != 0 :
                return False

    return True


def matrix_type(mat):
    if is_null(mat):
        return "This is a Null Matrix."

    if is_identity(mat):
        return "This is an Identity Matrix."

    if is_scaler(mat):
        return "This is a Scaler Matrix."

    if is_diagonal(mat):
        return "This is a Diagonal Matrix."

    if is_lower_triangular(mat):
        return "This is a Lower Triangular Matrix."

    if is_upper_triangular(mat):
        return "This is a Upper Triangular Matrix."

    if is_square(mat):
        return "This is a square matrix."

    return "This is neither Upper Triangular nor Lower Triangular and even not a Diagonal Matrix."


if __name__ == '__main__':
    matrix = initialize()

    print(matrix_type(matrix))


