import numpy as np

example_a = np.asarray([1,2,3,4])

def f(a = example_a, pos=2, element = 66):
    # Check if pos is within the valid range of indices
    if pos < 0 or pos > len(a):
        raise ValueError("Invalid position value")
    
    # Create a new array with one more element
    new_array = np.empty(len(a)+1)
    
    # Copy elements before the insertion position
    new_array[:pos] = a[:pos]
    
    # Insert the element at the specified position
    new_array[pos] = element
    
    # Copy elements after the insertion position
    new_array[pos+1:] = a[pos:]
    
    return new_array

a = f(a, pos=2, element=66)
print(a)