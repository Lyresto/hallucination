import numpy as np

x = np.array([-1, 2, 5, 100])
y = np.array([123, 456, 789, 1255])

# Create the A matrix for the least squares equation
A = np.column_stack([x**2, x, np.ones_like(x)])

# Solve the least squares equation
result, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

result = result.tolist()

result
