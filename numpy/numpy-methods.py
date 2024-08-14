import numpy as np
from numpy.random import Generator as gen, PCG64 as pcg

# todo Create a 1D array
arr = np.array([[1, 2, 3, 4, 5],
                [24, 12, 53, 24, 55]])
print("1D array:", arr[:, 1:3])

# todo Create a 2x3 array of zeros
zeros_arr = np.zeros((2, 3))
print("2x3 array of zeros:\n", zeros_arr)

# todo Create a 2x3 array of ones
ones_arr = np.ones((2, 3))
print("2x3 array of ones:\n", ones_arr)

# todo Create an array with values from 0 to 9
range_arr = np.arange(10)
print("Array with values from 0 to 9:", range_arr)

# todo Create an array with 5 values evenly spaced between 0 and 1
linspace_arr = np.linspace(0, 1, 5)
print("Array with 5 values evenly spaced between 0 and 1:", linspace_arr)

# todo Array created with np.full:
array_full = np.full((3, 4), 7)
print("Array created with np.full:")
print(array_full)

# todo Array created with np.empty:
array_empty = np.empty((3, 4))
print("Array created with np.empty:")
print(array_empty)

# todo Reshape a 1D array into a 2D array
reshaped_arr = np.arange(10).reshape((2, 5))
print("Reshaped 2D array:\n", reshaped_arr)

# todo Create a 2x2 array with random values between 0 and 1
random_arr = np.random.random((2, 2))
print("2x2 array with random values:\n", random_arr)

# todo Sum of all elements in the array
sum_arr = np.sum(arr)
print("Sum of all elements in the array:", sum_arr)

# todo Mean of all elements in the array
mean_arr = np.mean(arr)
print("Mean(avg) of all elements in the array:", mean_arr)

# todo Mean along axis 0:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

mean_axis_0 = np.mean(matrix, axis=0)
print("Mean(avg) along axis 0:(columns)", mean_axis_0)

# todo Mean along axis 1:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
mean_axis_1 = np.mean(matrix, axis=1)
print("Mean(avg) along axis 1:(rows)", mean_axis_1)

# todo Standard deviation of all elements in the array
std_arr = np.std(arr)
print("Standard deviation of all elements in the array:", std_arr)

# todo Calculate the peak to peak (range)
# Create an array
data = np.array([1, 2, 3, 4, 5])
range_value = np.ptp(data)
print("Peak to Peak:", range_value)

# todo Calculate the 50th percentile (median)
# Create an array
data = np.array([1, 2, 3, 4, 5])
percentile_50 = np.percentile(data, 50)
print("50th Percentile:", percentile_50)

# todo Calculate the 0.5 quantile (median)
# Create an array
data = np.array([1, 2, 3, 4, 5])
quantile_05 = np.quantile(data, 0.5)
print("0.5 Quantile:", quantile_05)

# todo Dot product of two 1D arrays
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
dot_product = np.dot(arr1, arr2)
print("Dot product of arr1 and arr2:", dot_product)

# todo Matrix multiplication of two 2D arrays
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matmul_result = np.matmul(matrix1, matrix2)
print("Matrix multiplication result:\n", matmul_result)

# todo Transpose a 2D array
transpose_arr = np.transpose(matrix1)
print("Transpose of matrix1:\n", transpose_arr)

# todo Inverse of a 2x2 matrix
inverse_matrix = np.linalg.inv(matrix1)
print("Inverse of matrix1:\n", inverse_matrix)

# todo Concatenate two 1D arrays
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated array:", concatenated_arr)

# todo Compute the covariance matrix
data = np.array([[23, 12, 30],
                 [41, 53, 26],
                 [71, 28, 19]])

# Compute the covariance matrix
cov_matrix = np.cov(data)
print("covariance", cov_matrix)

# todo Compute the correlation coefficient matrix
# Define the matrix
data = np.array([[23, 12, 30],
                 [41, 53, 26],
                 [71, 28, 19]])

# Compute the correlation coefficient matrix
corr_matrix = np.corrcoef(data, rowvar=False)

print('correlation', corr_matrix)

# todo Stack two 1D arrays vertically
vstack_arr = np.vstack((arr1, arr2))
print("Vertically stacked arrays:\n", vstack_arr)

# todo Stack two 1D arrays horizontally
hstack_arr = np.hstack((arr1, arr2))
print("Horizontally stacked arrays:", hstack_arr)
# todo Create an array of ones with the same shape and type
# Original array
original_array = np.array([[1, 2, 3], [4, 5, 6]])
ones_array = np.ones_like(original_array)
print("Original array:")
print(original_array)
print("\nOnes array created with np.ones_like:")
print(ones_array)

# todo Create an empty array with the same shape and type
original_array = np.array([[1, 2, 3], [4, 5, 6]])
empty_array = np.empty_like(original_array)

print("Original array:")
print(original_array)
print("\nEmpty array created with np.empty_like:")
print(empty_array)  # Values will be uninitialized

# todo Use np.minimum to find the element-wise minimum
# Create two arrays
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
# Use np.minimum to find the element-wise minimum
result = np.minimum(a, b)
print(result)

# todo Create a 1D array with 9 elements
new_arr = np.arange(9)

# todo Split the array into 3 sub-arrays
split_arr = np.split(new_arr, 3)
print("Split array into 3 sub-arrays:", split_arr)

array_j = gen(pcg())
print(array_j.normal(size=(5, 5)))
# todo Elements greater than 2
condition = arr > 2
where_arr = np.where(condition, arr, -1)
print("Elements greater than 2 (replaced by -1 if not):", where_arr)

# todo Unique elements in the array
unique_arr = np.unique(arr)
print("Unique elements in the array:", unique_arr)

simple_data = np.genfromtxt('../files/simple_data.csv', delimiter=',', dtype='str')
print("simple_data:", simple_data)
print('------------------------------------------------')
# todo numpy slicing types
# Create a NumPy array
arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [13, 22, 53, 74, 85, 16, 27, 28, 39]])
# Access the first row
first_row = arr[0]
print("Basic First Row:", first_row)

# Access the second column
second_column = arr[:, 1]
print("Basic Second Column:", second_column)
print('------------------------------------------------')
# Access every second element in the first row
stepwise_slice = arr[0, ::2]
print("Stepwise Slice of First Row:", stepwise_slice)

# Access every second element from both rows
stepwise_both = arr[:, ::2]
print("Stepwise Slice from Both Rows:", stepwise_both)
print('------------------------------------------------')
# Get elements greater than 20
conditional_slice = arr[arr > 20]
print("Elements Greater Than 20:", conditional_slice)

# Get elements in the first row that are even
even_elements_first_row = arr[0][arr[0] % 2 == 0]
print("Even Elements in First Row:", even_elements_first_row)

# SUPPORTED DATA TYPES BY NUMPY

# todo Integer Types:
#
# int8, int16, int32, int64: Signed integers of varying byte sizes.
# uint8, uint16, uint32, uint64: Unsigned integers of varying byte sizes.

# todo Floating Point Types:
#
# float16, float32, float64, float128: Floating-point numbers of varying precision.

# todo Complex Types:
#
# complex64, complex128, complex256: Complex numbers with varying precision.

# todo Boolean Type:
#
# bool: Represents Boolean values (True and False).

# todo String Type:
# str_: Fixed-length string type.
# unicode_: Fixed-length Unicode type.

# todo Object Type:
# object: General-purpose type to hold any Python object.

# todo Datetime and Timedelta Types:
# datetime64: Represents dates and times.
# timedelta64: Represents differences between dates and times.
