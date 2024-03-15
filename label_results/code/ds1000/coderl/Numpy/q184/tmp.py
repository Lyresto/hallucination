import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
from scipy import interpolate as intp
a, x_new, y_new = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy import interpolate as intp
x = []
y = []
for i in range(0,100):
    for j in range(0,100):
        x.append(i*2+j)
        y.append(j*2+i)
interp = intp.interp2d(x,y,a)
print(interp(0,0))



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
