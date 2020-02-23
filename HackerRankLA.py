import numpy as np

# A = np.array([[1,2,3],
#               [2,3,4],
#               [1,1,1]])
#
# B = np.array([[4,5,6],
#               [7,8,9],
#               [4,5,7]])
#
# C = (A - B).flatten()
#
# for elem in C:
#     print(elem)

# A = np.array([[1,2],
#               [2,3]])
# B = np.array([[4,5],
#               [7,8]])
#
# C = A @ B
#
# for elem in C.flatten():
#     print(elem)


# Find the solution [x, y] for the matrix equation xA + yI = -A^2, where x and y are scalars
A = np.array([[1,1,0], # 3x3 matrix
              [0,1,0],
              [0,0,1]])

I = np.identity(3) # 3x3 matrix

# Find solution of overdetermined system by least squares method
B = np.array([A.flatten(), I.flatten()]).transpose()  # 9x2 matrix
# z is the solution vector with dims 2x1
print(B)

c = -1*np.linalg.matrix_power(A, 2).flatten().transpose() # 9x1 matrix
print(c)

z = np.linalg.lstsq(B, c, rcond=-1)[0]
z = np.array(z)
print(z)

















