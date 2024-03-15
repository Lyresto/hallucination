import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def elementwise_function(element_1,element_2):
    return (element_1 + element_2)

z = [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 3]]
for i in range(0,3):
    for j in range(0,3):
        z[i][j] = elementwise_function(x[i][j],y[i][j])



#print(z)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(z, file)
