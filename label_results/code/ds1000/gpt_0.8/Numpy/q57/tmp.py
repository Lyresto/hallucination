import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
a = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np




def get_maximal_independent_vectors(matrix):
    # Perform row reduction using Gaussian elimination
    rref, _ = np.linalg.qr(matrix.T, mode='r')

    # Find the rows with leading coefficients
    leading_rows = np.where(np.abs(rref.diagonal()) > 1e-10)[0]

    # Extract the rows from the original matrix
    maximal_independent_vectors = matrix[leading_rows]

    return maximal_independent_vectors

a = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])
result = get_maximal_independent_vectors(a)
print(result)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
