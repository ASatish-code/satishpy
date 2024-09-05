import numpy as np
# Define matrices A, B, C using Python lists
A = [[3.7827, 3.3454, 3.2341],
     [2.2122, 3.5678, 3.9087],
     [1.1234, 2.8934, 5.9087]]

B = [[3.1234, 3.0987, 3.1234],
     [2.1111, 3.2222, 3.3333],
     [1.0987, 1.3456, 5.1234]]

C = [[3.1243, 3.0989, 3.1256],
     [2.6721, 3.6785, 3.9017],
     [1.1254, 2.8956, 5.9187]]

# Perform matrix addition
matrix_sum = [[A[i][j] + B[i][j] + C[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Perform matrix subtraction
matrix_diff = [[A[i][j] - B[i][j] - C[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Print the results
print("Matrix Addition (A + B + C):")
for row in matrix_sum:
    print(row)

print("\nMatrix Subtraction (A - B - C):")
for row in matrix_diff:
    print(row)


# Define matrices A, B, C using NumPy arrays
A = np.array([[3.7827, 3.3454, 3.2341],
              [2.2122, 3.5678, 3.9087],
              [1.1234, 2.8934, 5.9087]])

B = np.array([[3.1234, 3.0987, 3.1234],
              [2.1111, 3.2222, 3.3333],
              [1.0987, 1.3456, 5.1234]])

C = np.array([[3.1243, 3.0989, 3.1256],
              [2.6721, 3.6785, 3.9017],
              [1.1254, 2.8956, 5.9187]])

# Perform matrix addition
matrix_sum = A + B + C

# Perform matrix subtraction
matrix_diff = A - B - C

# Print the results
print("Matrix Addition (A + B + C):\n", matrix_sum)
print("\nMatrix Subtraction (A - B - C):\n", matrix_diff)
