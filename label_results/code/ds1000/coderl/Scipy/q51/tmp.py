
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.stats
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import scipy.stats
a = np.array([1., 2., 2.5, 4., 6.])
p, kurtosis = scipy.stats.kurtosis(a), scipy.stats.kurtosis(a, p=True)
print(kurtosis)



#print(kurtosis_result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(kurtosis_result, f)
