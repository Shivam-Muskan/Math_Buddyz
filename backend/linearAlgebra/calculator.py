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
    if not is_square(mat):
        return False

    for i in range(1, len(mat)):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True


def is_lower_triangular(mat):
    if not is_square(mat):
        return False

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
    if not is_square(mat):
        return False

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0 :
                return False
    return True


def is_scaler(mat):
    if not is_square(mat):
        return False

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i != j and mat[i][j] != 0 :
                return False

    for i in range(len(mat) - 1):
        if mat[i][i] != mat[i + 1][i + 1]:
            return False

    return True


def is_identity(mat):
    if not is_square(mat):
        return False

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
    dic = {'Null Matrix': is_null(mat), 'Square Matrix': is_square(mat), 'Identity Matrix': is_identity(mat),
           'Scaler Matrix': is_scaler(mat), 'Diagonal Matrix': is_diagonal(mat),
           'Lower Triangular Matrix': is_lower_triangular(mat), 'Upper Triangular Matrix': is_upper_triangular(mat)}

    return dic


if __name__ == '__main__':
    matrix = initialize()

    print(matrix_type(matrix))


