num = int(input("Total no. of matrices: "))
matrices = {}


def print_matrix(M, rowSize, colSize):
    for row_id in range(rowSize):
        for col in range(colSize):
            print(M[row_id][col], end=" ")
        print()


for i in range(1, num + 1):
    rows = int(input(f"No. of rows for Matrix {i} : "))
    cols = int(input(f"No. of columns in Matrix {i} : "))
    matrices[i] = [[0 for j in range(cols)] for k in range(rows)]
    print(matrices[i])
    print(f"Enter the elements of Matrix {i} : ")
    for k in range(rows):
        row = input('Enter a row: ')
        if len(row.split(sep=',')) == int(cols):
            matrices[i][k] = [int(x) for x in row.split(",")]
        else:
            continue
    print(matrices[i])
    print_matrix(matrices[i], rows, cols)

