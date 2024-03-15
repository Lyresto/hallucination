from itertools import zip_longest

def load_data():
	t = torch.fromnumpy(np.array(list(zip(*load_data_partial()))).reshape(3,-1))
	return [sum(t[i] * idx[i] for i in range(len(idx))) for i in range(3)]

def load_data_partial():
	# your code
	return list(zip_longest(*list(range(len(dtype))), fillvalue=-1))
