import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def one_hot(i, a):
    c = np.ones((2*i+1, 2*i+1), dtype=np.int)
    for j in range(i):
        c[j+1, a[j,0]] = 1
    return c.astype(np.int)




def encode_as_1_hot(i, a):
    c = np.zeros((2*i+1, 2*i+1), dtype=np.int)
    for j in range(i):
        c[j+1, a[j,0]] = 1
    return c



#print(b)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(b, file)
