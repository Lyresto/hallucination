import numpy as np
import pandas as pd
import torch
from torch.bmm import *

def solve(hid_dim, data, W):
	data = data.view(10, 2*3, hid_dim)
	W = W.view(10, hid_dim)
	return torch.bmm(data, W).squeeze()
