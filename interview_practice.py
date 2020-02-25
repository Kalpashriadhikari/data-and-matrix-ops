import numpy as np


def mprint(A):
    for i in A:
        print(i)
    print('\n')


# Dot product function
def dprod(v1, v2):
   return sum((a*b for a, b in zip(v1, v2)))


# Write a function to do matrix vector multiplication:
def mvprod(M, v):
    result = []
    for row in M:
        element = sum((a*b for a, b in zip(row,v)))
        result.append(element)
    return result

# Write a function that multiplies matrices
def mprod(M, N):
    mrows = len(M)
    ncols = len(N[0])
    result = [[] for i in range(mrows)]

    for i in range(mrows):
        for j in range(ncols):
            row = M[i]
            col = [nrow[j] for nrow in N]
            element = sum((r*c for r, c in zip(row, col)))
            result[i].append(element)
    return result

# transpose a matrix:
def transpose(M):
    cols = len(M[0])
    result = []
    for i in range(cols):
        tcol = [row[i] for row in M]
        result.append(tcol)
    return result

# Rotate a matrix 90 degrees clockwise
def rot90cw(M):
    nM = np.array(M)
    return np.flip(nM, 0).T

# Rotate a matrix 90 degrees ccw
def rot90ccw(M):
    numcols = len(M[0])
    temp = []
    final = []

    for i in range(numcols):
        temp.append([row[i] for row in M])

    numrows = len(temp)

    for j in range(numrows):
        final.append(temp[numrows - 1 - j])

    return final


# element wise sum of two vectors


# element wise difference of two vectors.


if __name__ == '__main__':

    # create a new ndarray from a nested list
    A = [[1,2,3],
        [2,4,6],
        [1,1,1]]

    B = [[1,2],
         [1,1],
         [1,3]]

    x = [1, 2]
    y = [1, 2, 3]
    z = [1, 1, 1]


    print("dot product using numpy and my function: ")
    print(dprod(y, z))
    print(np.dot(y,z), '\n')

    print("Matrix vector multiplication: ")
    mprint(mvprod(B, x))
    print(np.array(B) @ np.array(x), '\n')


    print("Matrix multiplication :")
    mprint(mprod(A, B))
    print(np.array(A) @ np.array(B), '\n')

    print("Transpose with numpy and my function:")
    mprint(transpose(B))
    print (np.transpose(np.array(B)), '\n')

    print("rotate matrix 90 degrees clockwise: ")
    mprint(B)
    mprint(rot90cw(B))

    #counter clock-wise
    print("rotate matrix 90 degrees counter-clockwise: ")
    mprint(B)
    mprint(rot90ccw(B))


    # print("sums two matrices: ")


    # print("differences")


    # matrix creation with numpy (random, zeros, ones, reshape)


    # finding maximum and minimum elements:


    # find row and column with highest total sum:


    # append sums of rows and columns to ndarray:


    # Matrix Powers


    # practice slicing lists and ndarrays (1-D)
    list1 = [0,1,2,3,4,5,6,7,8,9]


    #practice slicing 2-D (ndarray AND python list)


    # note that using slicing in numpy returns a view of the original ndarray. Any changes made to the slice
    # will be reflected in the original. In order to avoid this, try
