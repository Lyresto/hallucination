import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.stats
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.stats
a = np.random.randn(40)
b = 4*np.random.randn(50)
p_value = scipy.stats.ttest_1samp(a,b)

#print(p_value)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(p_value, file)
