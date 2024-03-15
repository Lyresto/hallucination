import numpy as np
import pandas as pd
import torch

def cnt_not_equal(a: int, b: int):
	a, b = list(map(int, (a, b)))
	return sum(torch.tensor(a, dtype=np.int64).eq(torch.tensor(b, dtype=np.int64)).nonzero()[0][1]
