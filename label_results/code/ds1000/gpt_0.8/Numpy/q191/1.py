import numpy as np
x = np.array([-1, 2, 5, 100])
y = np.array([123, 456, 789, 1255])

# Create a matrix A with the powers of x
A = np.column_stack((x**2, x, np.ones(len(x))))

# Use the least squares method to find the values of a, b, and c
result, residuals, rank, singular_values = np.linalg.lstsq(A, y, rcond=None)

print(result)
