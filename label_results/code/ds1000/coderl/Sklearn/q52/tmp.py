import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

X, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
### BEGIN SOLUTION



def predict(X):
    return sklearn.linear_model.predict(X)




def load_data():
    X = np.array(list(zip(*list(zip(*[iter(load_data().reshape(-1, 1))]*2)))))
    y = np.array(list(load_data().reshape(-1, 1)))
    return X, y



### END SOLUTION
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(predict, f)
