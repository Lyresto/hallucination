
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.fft as sf
N = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = sf.dct(np.eye(N), norm='ortho')



#print(result)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
