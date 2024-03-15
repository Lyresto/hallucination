import numpy as np
import torch

def np_array_to_torch_tensor(a):
	np_t = np.array(a, dtype=np.float32)
	torch_t = torch.from_numpy(np_t).float()
	return torch_t
