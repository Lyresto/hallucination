import numpy as np

# Define the function
def f(x, a, b, c):
    return a * x ** 2 + b * x + c

# Create the matrix A and the vector b
A = np.column_stack([np.square(x), x, np.ones(len(x))])
b = np.array(y)

# Solve the system of linear equations
result = np.linalg.lstsq(A, b, rcond=None)[0]

# Print the result
print(result)
END SOLUTION
