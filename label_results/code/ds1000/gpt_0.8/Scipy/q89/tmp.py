
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
from scipy import sparse
import numpy as np
import math
sa = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Convert the matrix to csr format
sa = sa.tocsr()

# Iterate through the columns
for col in range(sa.shape[1]):
    # Get the column data
    column = sa[:, col].data
    
    # Square each element in the column
    squared = [x**2 for x in column]
    
    # Calculate the length of the column
    length = math.sqrt(sum(squared))
    
    # Normalize the column by dividing each element by its length
    normalized = [x/length for x in column]
    
    # Update the original column in the matrix
    sa[:, col] = normalized



#print(sa)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(sa, f)
