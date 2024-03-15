import numpy as np
import pandas as pd
from torch import Tensor

def solve(a, b):
	# a, b = [torch.from_numpy(np.array(row)).cpu().numpy() for row in (a, b)]
	a = a.cpu().numpy()
	b = b.cpu().numpy()
	return torch.tensor(np.mean(a, b, axis=1)).numpy()
