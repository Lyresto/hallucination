import numpy as np

result = np.einsum('ijk,jl->ilk', A, B)
