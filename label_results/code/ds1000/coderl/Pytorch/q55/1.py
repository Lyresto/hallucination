def split_tensors(a, chunk_dim):
	return [a[i:i+chunk_dim] for i in range(0, len(a), chunk_dim)]
