def f(sA = example_sA):
	lil = lil_matrix(sA.copy(), shape = sA.shape)
	lil.make_symmetric()
	return lil
