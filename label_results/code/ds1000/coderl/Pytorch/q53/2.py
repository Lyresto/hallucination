import numpy as np
import pandas as pd
import torch

def cnt_not_equal(a, b):
	a = a.float()
	b = b.float()
	return sum(np.abs(a - b)!= np.abs(a - b).tolist())
