import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import numpy as np
import pandas as pd
import torch

a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def solve(a, b):
### BEGIN SOLUTION
    import numpy as np
    import pandas as pd
    from torch import Tensor
    
    


def solve(a, b):
    # a, b = [torch.from_numpy(np.array(row)).cpu().numpy() for row in (a, b)]
    a = a.cpu().numpy()
    b = b.cpu().numpy()
    return torch.tensor(np.mean(a, b, axis=1)).numpy()



### END SOLUTION
result = solve(a, b)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
