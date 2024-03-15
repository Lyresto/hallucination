import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
x, y, a, b = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
x = np.array([0, 1, 1, 1, 3, 1, 5, 5, 5])
y = np.array([0, 2, 3, 4, 2, 1, 3, 4, 5])
a = 1
b = 4
result =... # put solution in this variable
END SOLUTION
"""

"""
## Problem 2
"""

"""
Write a function that takes an array of integers and returns the index of the first element that satisfies the requirement.

For example, the index of (1, 4) would be 3: the elements at index 3 of x and y are 1 and 4 respectively.
A:
<code>
import numpy as np
x = np.array([0, 1, 1, 1, 3, 1, 5, 5, 5])
y = np.array([0, 2, 3, 4, 2, 1, 3, 4, 5])
a = 1
b = 4

#print(result)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
