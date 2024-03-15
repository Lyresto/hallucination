
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy.optimize import curve_fit
import numpy as np
z, Ua, tau, degree = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy.optimize import curve_fit
import numpy as np
s = '''1.000000000000000021e-03,2.794682735905079767e+02
4.000000000000000083e-03,2.757183469104809888e+02
1.400000000000000029e-02,2.791403179603880176e+02
2.099999999999999784e-02,1.781413355804160119e+02
3.300000000000000155e-02,-2.798375517344049968e+02
4.199999999999999567e-02,-2.770513900380149721e+02

#print(popt, pcov)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump([popt, pcov], f)
