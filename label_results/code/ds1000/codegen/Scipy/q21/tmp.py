
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
from scipy import sparse
c1, c2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
from scipy import sparse
c1 = sparse.csr_matrix([[0, 0, 1, 0], [2, 0, 0, 0], [0, 0, 0, 0]])
c2 = sparse.csr_matrix([[0, 3, 4, 0], [0, 0, 0, 5], [6, 7, 0, 8]])

#print(Feature)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(Feature, f)
