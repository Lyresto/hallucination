
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial.distance
example_array = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def f(example_array):

    result = scipy.spatial.distance.cdist(example_array, example_array)
    ### END SOLUTION
    return result

print(f(example_array))


result = f(example_array)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
