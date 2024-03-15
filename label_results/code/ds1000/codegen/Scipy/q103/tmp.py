
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import signal
arr, n = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy import signal
arr = np.array([-624.59309896, -624.59309896, -624.59309896,
                      -625., -625., -625.,])
n = 2
result = signal.find_extrema(arr, n)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
