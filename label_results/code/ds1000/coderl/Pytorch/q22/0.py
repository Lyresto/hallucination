from itertools import chain

def get_mask(lens):
	x = [1] * len(lens)
	return list(chain.from_iterable([[0] * i for i in range(len(lens))]))
