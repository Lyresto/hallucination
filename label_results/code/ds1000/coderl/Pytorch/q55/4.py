import numpy as np
import pandas as pd
import torch

def split_tensors(a, chunk_dim, keep_dim_size=True):
	if len(a.shape) == 1:
		return [a]
	a = a.contiguous().view(-1, chunk_dim**2)
	tensors = []
	for i, d in enumerate(a):
		s = 0
		if keep_dim_size:
			if i % len(a.shape) == 0:
				s = a[i]
			else:
				s = a[:i].view(-1)
		tensors.append([s])
		if i >= len(a.shape) - 1:
			break
	return tensors

def __starting_point():
	tensors = split_tensors(np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), 10)
	print(tensors)

__starting_point()
