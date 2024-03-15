
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.optimize as sciopt
import numpy as np
import pandas as pd
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Define the log-likelihood function for multinomial distribution
def multinomial_log_likelihood(weights, data):
    n = len(data)
    k = len(weights)
    log_likelihood = 0
    for i in range(k):
        log_likelihood += data.count(i) * np.log(weights[i])
    log_likelihood -= n * np.log(sum(weights))
    return -log_likelihood

# Use scipy.optimize.minimize to find the maximum likelihood estimate
initial_guess = np.ones(len(set(a['A1']))) / len(set(a['A1']))
result = sciopt.minimize(multinomial_log_likelihood, initial_guess, args=(a['A1'],))
weights = result.x

#print(weights)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(weights, f)
