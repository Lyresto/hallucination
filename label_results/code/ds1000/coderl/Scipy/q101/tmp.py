
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import scipy.optimize as sciopt
import numpy as np
import pandas as pd
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from collections import Counter
import numpy as np




def fit_multinomial(df, weights):
    n = len(df)
    
    dist = np.array([[0] * n for i in range(n)])
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = np.sum(df[i == j]) / (df[i].count(j) * weights[j])
    
    res = np.array([dist[i][j] for i in range(n) for j in range(n)])
    
    return res, dist
    



def multinomial_probability(df, weights):
    res, dist = fit_multinomial(df, weights)
    return res



#print(weights)



with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(weights, f)
