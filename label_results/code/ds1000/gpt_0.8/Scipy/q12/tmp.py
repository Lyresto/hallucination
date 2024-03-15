
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

from scipy import sparse
import numpy as np
sA, sB = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(sA, sB):
    from scipy import sparse
    import numpy as np
    
    # Create the sparse matrices
    m = np.array([[1,2,3],[4,5,6],[7,8,9]])
    c = np.array([0,1,2])
    m_sparse = sparse.csr_matrix(m)
    c_sparse = sparse.csr_matrix(c)
    
    # Perform the matrix multiplication
    result = m_sparse.dot(c_sparse)
    
    # Print the result
    print(result)
    



result = f(sA, sB)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
