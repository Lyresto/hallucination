
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.stats
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
kurtosis_result = scipy.stats.kurtosis(a)

#print(kurtosis_result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(kurtosis_result, f)
