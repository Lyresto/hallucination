
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial.distance
example_array = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.spatial.distance
example_array = np.array([[0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 2, 0, 2, 2, 0, 6, 0, 3,
#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
