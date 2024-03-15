import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
z = np.add(x, y)


#print(z)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(z, file)
