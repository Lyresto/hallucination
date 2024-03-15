import numpy as np
from scipy.sparse import csr_matrix
row = [2, 1]
column = [3, 0]
matrix = csr_matrix((np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))).todense()
#print(matrix[2, 3])
print(matrix[1, 0])
