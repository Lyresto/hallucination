import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

input = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
tf.compat.v1.disable_eager_execution()
###BEGIN SOLUTION
import tensorflow as tf


tf.compat.v1.disable_eager_execution()
input = [10, 20, 30]
result =... # put solution in this variable
END SOLUTION

"""

"""
## Exercise 2

"""

"""
### Exercise 2.1

"""

"""
Write a function that takes a list of integers and returns a list of the integers in the list sorted in ascending order.
"""


def sort_ascending(l):
  return sorted(l)


sort_ascending([1, 2, 3, 4, 5])


sort_ascending([1, 2, 3, 4, 5])

"""
### Exercise 2.2

"""

"""
Write a function that takes a list of integers and returns a list of the integers in the list sorted in descending order.
"""


def sort_descending(l):
  return sorted(l, reverse=True)


sort_descending([1, 2, 3, 4, 5])


sort_descending([1, 2, 3, 4, 5])

"""
### Exercise 2.3

"""

"""
Write a function that takes a list of integers and returns a list of the integers in the list sorted in random order.
"""


def sort_random(l):
  return sorted(l, key=lambda x: random.randint(0, len(l)-1))


sort_random([1, 2, 3, 4, 5])


sort_random([1, 2, 3, 4, 5])

"""
### Exercise 2.4

"""

"""
Write a function that takes a list of integers and returns a list of the integers in the list sorted in random order.
"""


def sort_random_reverse(l):
  return sorted(l, key=lambda x: random.randint(0, len(l)-1), reverse=True)


sort_random_reverse([1, 2, 3, 4, 5])


sort_random_reverse([1, 2, 3, 4, 5])

"""
### Exercise 2.5

"""

"""
Write a function that takes a list of integers and returns a list of the integers in the list sorted in random order.
"""


def sort_random_random(l):
  return sorted(l, key=lambda x: random.randint(0, len(l)-1), reverse=True, random_state=42)


sort_random_random
###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)