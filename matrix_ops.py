import numpy as np


def nprint(nested_list):
    for row in nested_list:
        print(' '.join(map(str, row)))
    print('\n')


def mproduct(A, B):
    a_rows = len(A)
    b_cols= len(B[0])

    C = [[0 for cols in range(b_cols)] for rows in range(a_rows)]

    for i in range(a_rows):
        for j in range(b_cols):
            a_row = A[i]
            b_col = [row[j] for row in B]
            C[i][j] = dot(a_row, b_col)

    return C


def transpose(M):
   return list(zip(*M))


def dot(v1, v2):
    if len(v1) == len(v2):
        product = 0
        for i in range(len(v1)):
            product += (v1[i] * v2[i])

        return product
    else:
        print("vectors are not equal in length")


def add(v1, v2):
    if len(v1) == len(v2):
        sum = []
        for i in range(len(v1)):
            sum.append(v1[i] + v2[i])

        return sum
    else:
        print("vectors are not equal in length")


def subtract(v1, v2):
    return add(v1, -1*v2)


if __name__ == '__main__':

    # create a new ndarray from a nested list
    matrix: np.ndarray = np.array([[1, 2, 3],
                                   [3, 5, 7],
                                   [7, 5, 3],
                                   [1, 2, 3]])

    print("Transpose with numpy and my function:")
    mT = matrix.transpose()
    mT2 = transpose(matrix)

    # print results of numpy and home-made transpose
    print(matrix, '\n')
    print(mT, '\n')
    print(mT2, '\n')


    print("dot product using numpy and my function: ")
    v1 = np.array([1, 2, 3])
    v2 = np.array([3, 5, 7])

    # dot product numpy method:
    product = np.dot(v1, v2)

    # dot product home made method:
    product2 = dot(v1, v2)

    # print results
    print(product)
    print(product2, '\n')

    print("sums: ")
    print(v1 + v2)
    print(add(v1, v2), '\n')

    print("differences")
    print(v1 - v2)
    print(subtract(v1, v2), '\n')

    print("Matrix multiplication with numpy built-in and my own function:")
    C = mproduct(matrix, mT)
    nprint(C)
    print(matrix @ mT)

    # matrix creation
    mzeros = np.zeros((3, 4))
    print(mzeros, '\n')

    mones = np.ones((3, 4))
    print(mones, '\n')

    mrand = np.random.random((3, 3))
    print(mrand, '\n')

    # finding maximum and minimum elements:
    print("Maximum element: {} ".format(matrix.max()))
    print("Minimum element: {} ".format(matrix.min()))

    # find row and column with highest total sum:
    sums = [row.sum() for row in matrix]
    csums = [col.sum() for col in matrix.transpose()]


    print("Highest sum of elements in a row occurs in row {}".format(np.argmax(sums)))
    print("Highest sum of elements in a column occurs in column {} \n".format(np.argmax(csums)))

    # append sums of rows and columns to ndarray:
    insert_before = len(matrix)
    data = np.insert(matrix, insert_before, csums, axis=0)

    print(matrix)
    print(data)