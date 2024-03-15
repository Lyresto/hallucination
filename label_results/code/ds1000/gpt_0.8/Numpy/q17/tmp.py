import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import numpy as np

# Set the random seed to ensure reproducibility
np.random.seed(0)

# Generate the random array
r = np.random.randint(3, size=(100, 2000)) - 1

# Save the random array as r_old
r_old = r.copy()

# Generate a new random array using the same seed
r_new = np.random.randint(3, size=(100, 2000)) - 1

# Check if the arrays are the same
print(np.array_equal(r_old, r_new))


#print(r_old, r_new)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump([r_old, r_new], file)
