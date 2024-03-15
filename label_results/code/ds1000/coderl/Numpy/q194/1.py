import numpy as np
a = np.empty((5, 6, 3))
np.multiply(a, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
np.einsum('ijk,jl->ilk', a, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
