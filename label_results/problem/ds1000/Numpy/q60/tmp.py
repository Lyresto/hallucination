import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]
t, p_value = scipy.stats.ttest_ind(a, b, equal_var=False)

#print(p_value)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(p_value, file)
