
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy import sparse
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy import sparse
import numpy as np
a = np.ones((2, 2))
b = sparse.csr_matrix(a)
b =... # put solution in this variable
END SOLUTION

"""
<|python|>#
#print(b)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(b, f)
