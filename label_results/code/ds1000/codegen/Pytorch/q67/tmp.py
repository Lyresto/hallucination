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
import numpy as np
import pandas as pd
import torch
hid_dim = 32
data = torch.randn(10, 2, 3, hid_dim)
data = data.view(10, 2 * 3, hid_dim)
W = torch.randn(hid_dim)

### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
