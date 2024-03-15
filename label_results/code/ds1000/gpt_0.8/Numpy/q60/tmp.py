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

# Remove NaN values from the original data arrays
a = a[~np.isnan(a)]
b = b[~np.isnan(b)]

# Perform the two-tailed t-test
t_stat, p_value = scipy.stats.ttest_ind(a, b, equal_var=False)

print("p-value:", p_value)



#print(p_value)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(p_value, file)
