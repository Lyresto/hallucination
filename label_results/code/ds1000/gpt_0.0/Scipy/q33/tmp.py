
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.ndimage
square = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Using binary erosion and dilation to remove isolated single cells
square = np.zeros((32, 32))
square[10:-10, 10:-10] = np.random.randint(1, 255, size = (12, 12))
np.random.seed(12)
x, y = (32*np.random.random((2, 20))).astype(int)
square[x, y] = np.random.randint(1, 255, size = (20,))

# Define a structuring element for binary erosion and dilation
selem = np.array([[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]])

# Perform binary erosion and dilation to remove isolated single cells
eroded = scipy.ndimage.binary_erosion(square > 0, structure=selem)
dilated = scipy.ndimage.binary_dilation(eroded, structure=selem)

# Set values to 0 where the original array is nonzero and the dilated array is 1
square[(square > 0) & (dilated == 1)] = 0
END SOLUTION

#print(square)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(square, f)
