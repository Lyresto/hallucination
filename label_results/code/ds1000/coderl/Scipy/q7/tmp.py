
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np

import scipy.stats
z_scores, mu, sigma = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

import scipy.stats




def ddnxt(a, b, n):
    return (a + b) / n




def approx_pvalue(z_scores, mu, sigma):
    sigma2 = sigma ** 2
    df = ddnxt(sigma2, sigma2 - mu, len(z_scores) - 1)
    acf = np.cumsum(z_scores) / df
    p_values = scipy.stats.norm.pdf(acf, mu, sigma).round()
    return p_values



#print(p_values)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(p_values, f)
