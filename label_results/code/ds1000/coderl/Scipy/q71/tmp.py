
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy.spatial import distance
shape = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def get_distance_2(y, x):
    #your code here
    a,b,c,d = [],[],[],[]
    for i in range(6):
        for j in range(6):
            a.append(sum((y[i,j]-x[i,j])**2))
    for i in range(6):
        for j in range(6):
            c.append(sum((y[i,j]-x[i,j])**2))
    for i in range(6):
        for j in range(6):
            d.append(sum((y[i,j]-x[i,j])**2))
    return a,b,c,d



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
