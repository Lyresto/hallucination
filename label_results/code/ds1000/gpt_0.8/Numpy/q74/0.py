import numpy as np

def insert_element(array, index, element):
    return np.insert(array, index, element)

example_a = np.asarray([1, 2, 3, 4])
new_a = insert_element(example_a, 2, 66)
print(new_a)