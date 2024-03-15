import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import interpolate as intp
a, x_new, y_new = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Define the x and y coordinates of the original array
x = np.linspace(0, 2, 2)
y = np.linspace(0, 2, 2)

# Create a meshgrid of the original coordinates
X, Y = np.meshgrid(x, y)

# Create a meshgrid of the new coordinates
X_new, Y_new = np.meshgrid(x_new, y_new)

# Flatten the original array and create a 1D array of the values
z = a.flatten()

# Create a 2D interpolation function
f = intp.interp2d(X, Y, z, kind='linear')

# Use the interpolation function to interpolate the new values
result = f(X_new, Y_new)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
