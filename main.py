import numpy as np

# todo 1. Matrix Example
# Creating a 2x3 matrix
matrix = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

matrix2 = np.array([[1, 2],
                    [4, 9],
                    [2, -2]])
x = np.array([2, -23, 3])
y = np.array([-2, 2, 8])
print("Matrix:")
print(matrix.shape)
print(matrix2.shape)
print(x.shape)

# todo 2. Vector Examples
# Creating a row vector
row_vector = np.array([[1, 2, 3]])

print("Row Vector:")
print(row_vector)

# Creating a column vector
column_vector = np.array([[1], [2], [3]])

print("Column Vector:")
print(column_vector)

# todo 3. Scalar Example
# Creating a scalar
scalar = 5

print("Scalar:")
print(scalar)

print(type(matrix))
print(type(row_vector))
print(type(column_vector))
print(type(scalar))
# Get dimensions
print("Dimensions of matrix:", matrix.ndim)  # Should be 2
print("Dimensions of row vector:", row_vector.ndim)  # Should be 2
print("Dimensions of column vector:", column_vector.ndim)  # Should be 2
print("Dimensions of scalar:", np.array(scalar).ndim)  # Should be 0
# Transpose the Column Vector
transposed_column_vector = column_vector.T
print("Transposed Column Vector:")
print(transposed_column_vector)
print('---------------------------------------------')
# print(np.dot(matrix, matrix2))
# shape = np.dot(matrix, matrix2).shape
# print(shape)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Define a 4x5 matrix
matrix_a = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20]])

# Define a 5x3 matrix
matrix_b = np.array([[1, 2, 2],
                     [3, 4, -3],
                     [5, 6, -22],
                     [7, 8, 9],
                     [9, 10, 10]])

# Calculate the dot product (matrix multiplication) which is 4*3 in result
dot_product = np.dot(matrix_a, matrix_b)
print("Dot Product of 4x5 and 5x3 matrices:")
print(dot_product)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Define a 3x4 matrix
matrix_a = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])

# Define a 4x2 matrix
matrix_b = np.array([[1, 2],
                     [3, 4],
                     [5, 6],
                     [7, 8]])

# Calculate the dot product (matrix multiplication) which is 3*2
dot_product = np.dot(matrix_a, matrix_b)

print("Dot Product of 3x4 and 4x2 matrices :")
print(dot_product)

# todo Compatibility Rules
# For two matrices to be multiplied (dot product), the number of columns in the first matrix must equal the number of rows in the second matrix.
#
# Matrix A:
# 3
# ×
# 4
# 3×4 (3 rows, 4 columns)
# Matrix B:
# 2
# ×
# 3
# 2×3 (2 rows, 3 columns)
# Since the first matrix has 4 columns and the second matrix has 2 rows, they cannot be multiplied together.
