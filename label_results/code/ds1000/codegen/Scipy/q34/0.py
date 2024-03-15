import numpy as np
from scipy.sparse import csr_matrix

np.random.seed(10)
arr = np.random.randint(4,size=(988,988))
sA = csr_matrix(arr)
col = sA.getcol(0)
mean, standard_deviation =... # put solution in these variables
BEGIN SOLUTION
