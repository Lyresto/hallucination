
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.optimize as sciopt
import numpy as np
import pandas as pd
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import scipy.optimize as sciopt
import numpy as np
import pandas as pd




def multinomial_negative_log_likelihood(params, frequencies):
    n = np.sum(frequencies)
    log_likelihood = np.sum(frequencies * np.log(params))
    return -log_likelihood

a = pd.DataFrame({'A1':[0,1,2,3,2,1,6,0,1,1,7,10]})
frequencies = a['A1'].values

# Initial guess for the parameters
params_initial = np.ones(len(np.unique(frequencies))) / len(np.unique(frequencies))

# Define the bounds for the parameters (probabilities should be between 0 and 1)
bounds = [(0, 1)] * len(params_initial)

# Minimize the negative log-likelihood function
result = sciopt.minimize(multinomial_negative_log_likelihood, params_initial, args=(frequencies,), bounds=bounds)

# Extract the estimated parameters
weights = result.x

print("Estimated parameters:")
for i, weight in enumerate(weights):
    print(f"Category {i}: {weight:.3f}")



#print(weights)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(weights, f)
