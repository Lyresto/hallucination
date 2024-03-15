import numpy as np

def f(a, pos, element):
    return np.insert(a, pos, element)

example_a = np.asarray([1,2,3,4])
new_a = f(example_a, pos=2, element=66)
print(new_a)

# Output: [ 1  2 66  3  4]