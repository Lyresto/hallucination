import torch

def convert_array_to_tensor(a):
	a_pt = []
	for x in a:
		a_pt.append(torch.from_numpy(x))
	return a_pt
