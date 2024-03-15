
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial
import scipy.optimize

points1, N, points2 = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
# Define the cost function to minimize
def cost_function(assignment, points1, points2):
    total_distance = 0
    for i in range(len(assignment)):
        total_distance += scipy.spatial.distance.cityblock(points1[i], points2[assignment[i]])
    return total_distance

# Define the constraints for the optimization problem
constraints = []
for i in range(N):
    constraints.append({'type': 'eq', 'fun': lambda x, i=i: np.sum(x == i) - 1})
for j in range(N):
    constraints.append({'type': 'eq', 'fun': lambda x, j=j: np.sum(x == j) - 1})

# Solve the optimization problem
initial_guess = np.arange(N)
result = scipy.optimize.minimize(cost_function, initial_guess, args=(points1, points2), method='SLSQP', constraints=constraints)
result = result.x.astype(int)

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)
