def csr_matrix(a):
	ar = []
	for i,j in zip(a.row,a.col):
		if i!=j: ar.append(i),ar.append(j)
	return sparse.csr_matrix((ar),(len(a),len(a[0]))).toarray()
