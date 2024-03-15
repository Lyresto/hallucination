import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a, index = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.arange(1,11)
index = np.array([0,1,0,0,0,1,1,2,2,1])
result = a[index]
print(result)



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
