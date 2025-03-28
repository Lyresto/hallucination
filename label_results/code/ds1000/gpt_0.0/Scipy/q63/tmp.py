
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.fft as sf
N = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        if i == 0:
            result[i,j] = np.sqrt(1/N)
        else:
            result[i,j] = np.sqrt(2/N) * np.cos((np.pi/N) * (j + 0.5) * i)

#print(result)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
