
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
from scipy import sparse
import numpy as np
import math
sa = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np

class WeightMatrix:

    


def __init__(self, weight_matrix):
    weight_matrix = np.array(weight_matrix)
    self.__WeightMatrix__ = weight_matrix
    self.shape = weight_matrix.shape




def __mul__(self, other):
    if type(other)!= WeightMatrix:
        return NotImplemented
    weight_matrix = self.__WeightMatrix__
    for i in range(self.shape[1]):
        other.__WeightMatrix__[:,i] = (weight_matrix[:,i] * other.__WeightMatrix__[:,i]).normalize()
    return other



#print(sa)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(sa, f)
