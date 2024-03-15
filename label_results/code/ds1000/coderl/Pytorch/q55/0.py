from itertools import groupby
def tensors_31(a):
	chunk_dim = 10
	tensors = []
	for group in groupby(a, key=len):
		values = [list(j) for j in group]
		split = tuple(zip(*values))
		tensors.append(split)
	return tensors
