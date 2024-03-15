
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import signal
arr, n = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Using scipy.signal.argrelextrema to find local minima and maxima
maxima_indices = signal.argrelextrema(arr, np.greater_equal, order=n)[0]
minima_indices = signal.argrelextrema(arr, np.less_equal, order=n)[0]

# Combining the indices and sorting them in ascending order
result = np.sort(np.concatenate((maxima_indices, minima_indices)))

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
