import numpy as np
import torch
idx, B = load_data()

C =... # put solution in this variable

def index_select(ind, col_slice):
	out = []
	for i in col_slice:
		if i in ind:
			out.append(ind[i])
		else:
			out.append(np.array([]))
	return torch.LongTensor(out)
