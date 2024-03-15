import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np



def select_elements(a, b):
    N, M = a.shape
    target = np.zeros((N, M), dtype=np.int)
    for n, i in enumerate(b):
        target[n, i] = np.argwhere(a == i)[0].tolist()
    return target



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
