import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x_dists, y_dists = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
dists = np.stack((x_dists, y_dists), axis=2)

#print(dists)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(dists, file)
