
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
from scipy.sparse import lil_matrix



def f(sA):
    import numpy as np
    from scipy.sparse import lil_matrix
    
    


def make_symmetric(sA):
    n = sA.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            if sA[i, j] != 0 and sA[j, i] == 0:
                sA[j, i] = sA[i, j]
    return sA

# Example usage
example_sA = lil_matrix((10, 10))
example_sA[1, 3] = 2
example_sA[3, 1] = 3

print("Before making symmetric:")
print(example_sA.toarray())

symmetric_sA = make_symmetric(example_sA)

print("After making symmetric:")
print(symmetric_sA.toarray())



sA = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))

result = f(sA)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
