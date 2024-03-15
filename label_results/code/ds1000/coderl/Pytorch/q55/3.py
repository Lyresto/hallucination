from itertools import groupby
from numpy import chunks

def chunks_sum(iterable, size):
	iterable = iter(iterable)
	return sum(sum(chunks(iterable, size), ()) / size)

def split_tensors_by_step(tensors, chunk_dim):
	return [list(g) for _, g in groupby(tensors, key=chunks_sum)]
