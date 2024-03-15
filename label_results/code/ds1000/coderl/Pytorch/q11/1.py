import numpy as np
import torch

def load_data():
	a, b = np.array(np.load('data.npy')).T
	a_log = a[b!= 0]
	b_truncated = b[a_log!= 0]
	return torch.LongTensor(b_truncated)[:, a_log]
