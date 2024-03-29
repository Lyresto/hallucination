
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy.optimize import curve_fit
import numpy as np
z, Ua, tau, degree = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def fourier(x, *coefficients):
    result = 0
    for i in range(len(coefficients)):
        result += coefficients[i] * np.cos((i+1) * np.pi / tau * x)
    return result

popt, pcov = curve_fit(fourier, z, Ua, p0=[1] * degree)



#print(popt, pcov)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump([popt, pcov], f)
