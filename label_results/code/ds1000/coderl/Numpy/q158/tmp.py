import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x_dists, y_dists = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np



def dist(x, y):
    return np.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)



def dist_pairs(x, y):
    return list(zip(dist(x, y), dist(y,x)))



#print(dists)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(dists, file)
