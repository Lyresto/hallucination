
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial
import scipy.optimize

points1, N, points2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
import scipy.spatial
import scipy.optimize

# Define the cost matrix
cost_matrix = scipy.spatial.distance.cdist(points1, points2, metric='cityblock')

# Use the Hungarian algorithm to find the optimal assignment
row_ind, col_ind = scipy.optimize.linear_sum_assignment(cost_matrix)

# Get the assignment as a list
assignment = col_ind.tolist()

# Print the assignment
print(assignment)



#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
