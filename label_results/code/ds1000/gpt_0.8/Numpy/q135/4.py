To convert the integers to binary numpy arrays of length m, you can use the `np.binary_repr()` function from NumPy. This function returns the binary representation of a number as a string.

Here's a code snippet that demonstrates how to achieve this:

```python
import numpy as np

def convert_to_binary(num, m):
    binary_str = np.binary_repr(num, width=m)
    binary_array = np.array(list(binary_str), dtype=int)
    return binary_array

a = np.array([1, 2, 3, 4, 5])
m = 6

result = np.zeros((len(a), m), dtype=int)
for i, num in enumerate(a):
    result[i] = convert_to_binary(num, m)
```

In this code, the `convert_to_binary()` function takes a number `num` and a desired length `m` as input. It uses `np.binary_repr()` to convert the number to its binary representation as a string. Then, it converts the string to a numpy array of integers using `np.array()` and sets the desired data type to `int`.

The code initializes the `result` array with zeros of shape (n, m), where n is the length of array `a`. It then iterates over each element in `a`, calls the `convert_to_binary()` function to get the binary representation as a numpy array, and assigns it to the corresponding row of the `result` array.

The resulting `result` array will be a (n, m) matrix where each row represents the binary representation of the corresponding integer in `a`.