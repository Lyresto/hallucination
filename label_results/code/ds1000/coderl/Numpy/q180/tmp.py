import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
Z = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
Z = np.random.rand(*np.random.randint(2, 10, (np.random.randint(2, 10))))
ans = np.zeros_like(Z)




def slicing(Z):
    #...
    ans[:] = Z[:]
    if Z.ndim == 1:
        return Z[0]
    if Z.ndim == 2:
        return Z[:,0]
    return Z[:,:,0]



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
