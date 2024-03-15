from scipy.sparse import csr_matrix
mat = csr_matrix(([float(i) for i in row] for row in arr),shape=(len(arr),len(arr[0])))
print(mat[1,0])
