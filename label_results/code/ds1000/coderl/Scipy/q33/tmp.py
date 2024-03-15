
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.ndimage
square = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.ndimage
square = np.zeros((32, 32))
np.random.seed(12)
x, y = (32*np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size = (20,))
square = square.astype(int)
res = scipy.ndimage.binary_fill_holes(square)



#print(square)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(square, f)
