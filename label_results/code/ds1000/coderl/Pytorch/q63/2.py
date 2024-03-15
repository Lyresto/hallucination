import numpy as np
import pandas as pd
from torch import *
def solve(a, b):
	t1 = [list(i) for i in zip(*zip(a, b))]
	t2 = [list(i) for i in zip(*zip(b, a))]
	t = torch.cat(t1, t2)
	return t.tolist()
