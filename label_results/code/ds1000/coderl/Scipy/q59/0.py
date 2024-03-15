import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
M = csr_matrix(arr)
r = M.getrow(row)
c = M.getcol(column)
