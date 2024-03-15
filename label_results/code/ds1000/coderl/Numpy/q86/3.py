import numpy as np


def torch_to_numpy(t, force_cpu=False):
	if force_cpu:
		t = t.cpu()
	return np.array(t.numpy())
