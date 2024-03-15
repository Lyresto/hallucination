import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
x = np.array([1400, 1500, 1600, np.nan, np.nan, np.nan,1700])

#print(x)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(x, file)
