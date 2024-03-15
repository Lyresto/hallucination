
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy.optimize import curve_fit
import numpy as np
z, Ua, tau, degree = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import sys




def func(x, a1, a2):
    return a1 * np.cos(1 * np.pi / a1 * x) + \
       a2 * np.cos(2 * np.pi / a2 * x)




def func_coords(x, a1, a2):
    return a1 * np.cos(1 * np.pi / a1 * x) + \
           a2 * np.cos(2 * np.pi / a2 * x)

# import and filename
filename = 'data.txt'
import numpy as np

# read the data
z, Ua = np.loadtxt(filename,delimiter=',', unpack=True)

# default values for the coordinates
a1 = 1.0
a2 = 0.0

# first fit using numpy.least_squares
popt, pcov = np.least_squares(func, a1, a2)

# and using scipy.optimize
x = np.linspace(0, 4.0*np.pi/tau, 2000)

# compare with scipy.least_squares
y = func(x, *popt)
print(f'least_squares: ({popt}, {pcov})')
print(f'y: {y}')



#print(popt, pcov)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump([popt, pcov], f)
