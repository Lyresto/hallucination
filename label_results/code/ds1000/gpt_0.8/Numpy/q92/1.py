import numpy as np
a = np.array([4, 1, 0, 8, 5, 2])
N = 3

# Get the indices of the N largest elements
indices = np.argpartition(a, -N)[-N:]

# Sort the indices in decreasing order
result = indices[np.argsort(-a[indices])]

print(result)