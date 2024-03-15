
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import signal
arr, n = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy import signal



def relative_extrema(arr, n):
    return [i for i in range(len(arr)) if signal.convolve2d(arr[i:],[1,-1][n&1],mode='same') < 0]



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
