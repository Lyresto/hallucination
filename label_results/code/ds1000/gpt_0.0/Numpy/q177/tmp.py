import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, size = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from numpy.lib.stride_tricks import as_strided

# pad the array with zeros to handle edge effects
padded = np.pad(a, ((size[0]//2, size[0]//2), (size[1]//2, size[1]//2)), mode='constant')

# create a view into the padded array with the desired window size and stride
view = as_strided(padded, shape=(a.shape[0], a.shape[1], size[0], size[1]), strides=padded.strides + padded.strides)

# reshape the view to get a series of arrays
result = view.reshape(-1, size[0], size[1])



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
