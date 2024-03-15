from scipy import sparse
c1 = sparse.csr_matrix([[0, 0, 1, 0], [2, 0, 0, 0], [0, 0, 0, 0]])
c2 = sparse.csr_matrix([[0, 3, 4, 0], [0, 0, 0, 5], [6, 7, 0, 8]])
c = c1 + c2
print(c.todense())
