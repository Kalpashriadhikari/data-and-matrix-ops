import numpy as np
import sympy as sp

def mprint(A):
    for i in A:
        print(i)
    print('\n')


# Dot product function from scratch


# Write a function to do matrix vector multiplication from scratch:


# Write a function that multiplies matrices


# transpose a matrix:


# Rotate a matrix 90 degrees clockwise (using numpy)


# Rotate a matrix 90 degrees ccw


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

    print("Matrix vector multiplication: ")

    print("Matrix multiplication :")

    print("Transpose with numpy and my function:")

    print("rotate matrix 90 degrees clockwise: ")

    print("rotate matrix 90 degrees counter-clockwise: ")

    # matrix creation with numpy (random, zeros, ones, reshape)
    print("practice with ndarray creation using random, zeros, ones and reshape")

    # show that numpy.reshape and ndarray.reshape both return reshaped references to the original object, not a copy.

    # finding maximum and minimum elements:

    print("find the maximum sum along rows and columns")

    print("practice appending rows and columns, using the sums above")

    print("X with sums appended as an additional row or column:")

    # Matrix Powers

    # practice slicing lists (1-D) (works the same for Numpy ndarrays)

    #slicing lists in 2-D (must use list comprehension, as 2-D slicing is unavailable for lists)

    # practice slicing 2-D with Numpy ndarrays (recreate list3 but with better slicing capabilities)

    # ***NOTE*** that using slicing in numpy returns a view of the original ndarray. Any changes made to the slice
    # will be reflected in the original. In order to avoid this, you must make a copy.


