
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.fft as sf
N = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.fft as sf




def dctmtx(N):
    # your code here
    z = np.zeros(N)
    for i in range(N):
        z[i] = (i+1) * np.sin(2*np.pi/N*i) / (2*i)
    return np.real(sf.dctn(z))



#print(result)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
