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
    from sklearn.preprocessing import MultiLabelBinarizer
    
    features = [
        ['f1', 'f2', 'f3'],
        ['f2', 'f4', 'f5', 'f6'],
        ['f1', 'f2']
    ]
    
    


def solve(features):
    mlb = MultiLabelBinarizer()
    new_features = mlb.fit_transform(features)
    return new_features

new_features = solve(features)
print(new_features)



### END SOLUTION
new_features = solve(features)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_features, f)
