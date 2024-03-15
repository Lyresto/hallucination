from scipy.sparse.csgraph import csgraph_from_dense, square

def get_result(s):
	v = pipe.named_steps["tf_idf"]
	return csgraph_from_dense(square(v.fit_transform(s.test.values)), sparse=False).todense()
