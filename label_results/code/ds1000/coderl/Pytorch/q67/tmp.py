import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

torch.random.manual_seed(42)
hid_dim = 32
data = torch.randn(10, 2, 3, hid_dim)
data = data.view(10, 2 * 3, hid_dim)
W = torch.randn(hid_dim)
### BEGIN SOLUTION
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



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
