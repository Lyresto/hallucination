import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
X = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(X):

    result = []
    for i in range(len(X)):
        result.append(X[i])
    ### END SOLUTION
    return result


result = f(X)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
