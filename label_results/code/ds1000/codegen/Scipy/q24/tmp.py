
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial
import scipy.optimize

points1, N, points2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
points1 = np.array([(x, y) for x in np.linspace(-1,1,7) for y in np.linspace(-1,1,7)])
N = points1.shape[0]
points2 = 2*np.random.rand(N,2)-1
result =... # put solution in this variable

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
