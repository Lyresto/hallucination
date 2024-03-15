import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.array([[1,2,8],
     [7,4,2],
     [9,1,7],
     [0,1,5],
     [6,4,3]])
result =... # put solution in this variable
END SOLUTION
"""

import numpy as np
import math

def pdist(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_2(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_3(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_4(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_5(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_6(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_7(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_8(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_9(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_10(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def euclidean_dist_11(a, b):
    """
    Calculate the Euclidean distance between two points.
    """
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
