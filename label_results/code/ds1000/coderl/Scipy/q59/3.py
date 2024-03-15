#from numpy import csr_matrix
#A = csr_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#print(A.getrow(2))
#print(A[1, 0])

import numpy as np
import scipy.sparse as sp
x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
y = [3,0]
z = sp.csr_matrix(x).getrow(y)
print(z)
