import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

features = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def solve(features):
### BEGIN SOLUTION
    import numpy as np
    
    


def solve(features):
    X = np.zeros((len(features), len(features[0])), dtype=object)
    for i in range(len(X)):
        for j in range(len(features[i])):
            X[i, features[i][j]] = 1
    return X



### END SOLUTION
new_features = solve(features)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_features, f)
