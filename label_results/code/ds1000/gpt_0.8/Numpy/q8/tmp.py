import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

a = np.array([[1,0,3], [2,4,1]])
n = np.max(a) + 1

b = np.zeros((a.shape[0], n))
b[np.arange(a.shape[0])[:, np.newaxis], a] = 1

print(b)


#print(b)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(b, file)
