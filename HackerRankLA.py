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
# A = np.array([[1,1,0], # 3x3 matrix
#               [0,1,0],
#               [0,0,1]])
#
# I = np.identity(3) # 3x3 matrix
#
# # Find solution of overdetermined system by least squares method
# B = np.array([A.flatten(), I.flatten()]).transpose()  # 9x2 matrix
# # z is the solution vector with dims 2x1
# print(B)
#
# c = -1*np.linalg.matrix_power(A, 2).flatten().transpose() # 9x1 matrix
# print(c)
#
# z = np.linalg.lstsq(B, c, rcond=-1)[0]
# z = np.array(z)
# print(z)

# # solve A^1000
# A = np.array([[-2, -9],
#               [1, 4]])

# print(np.linalg.matrix_power(A, 1000))

# # Find the eigenvalues
# A = np.array([[0,1],
#               [-2, -3]])
#
# print(np.linalg.eigvals(A))

# # Find the determinant of a matrix
# A = np.array([[3,0,0,-2,4],
#               [0,2,0,0,0],
#               [0,-1,0,5,-3],
#               [-4,0,1,0,6],
#               [0,-1,0,3,2]])

# print(np.linalg.det(A))

# Diagonalize A:

A = np.array([[-2, -9],
              [1, 4]])

# step 1. Is it possible? For an nxn matrix, there must be n unique eigenvalues:
vals, vects = np.linalg.eig(A)
vals2 = np.linalg.eigvals(A)

#Show 5 distinct eigenvalues
print("Eigenvalues: ", vals)
print("linalg.eigvals: ", vals2)

print("Eigenvectors: ", vects)


















