import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
X = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(X):
    result = []
    for row in X:
        for element in row:
            result.append(element)
    return result
    ### END SOLUTION

result = f(X)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
