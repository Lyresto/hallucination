
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np

import scipy.stats
z_scores, mu, sigma = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

p_values = scipy.stats.norm.cdf(z_scores, loc=mu, scale=sigma)



#print(p_values)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(p_values, f)
