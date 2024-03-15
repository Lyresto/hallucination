from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd
import torch
from torch import bmm

hid_dim = 32
data = torch.randn(10, 2, 3, hid_dim)
data = data.view(10, 2*3, hid_dim)
W = torch.randn(hid_dim) # assume trainable parameters via nn.Parameter
res = torch.bmm(data, W).squeeze()
res = res.view(10, 2, 3)
