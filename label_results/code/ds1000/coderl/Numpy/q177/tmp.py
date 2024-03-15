import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from numpy import array, window




def sliding_window(a, size, center=None):
    if center is None:
        center = (size[0]//2, size[1]//2)
    return [array(window(a[i*size[0]:(i+1)*size[0], center=center, axis=i))
    for i in range(size[0])]



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
