import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
a = np.array([4, 1, 0, 8, 5, 2])
res = [2,1,5,0,4,3]
print(np.argsort(a))



#print(result)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)