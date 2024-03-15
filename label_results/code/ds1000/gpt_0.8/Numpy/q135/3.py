One way to solve this problem is to use the bitwise shift and bitwise AND operations in numpy.

Here's one possible solution:

```python
import numpy as np

def convert_to_binary(num, m):
    binary = np.unpackbits(np.array([num], dtype=np.uint8))
    return binary[-m:]

a = np.array([1, 2, 3, 4, 5])
m = 6
result = np.zeros((len(a), m), dtype=int)

for i, num in enumerate(a):
    if num < 0:
        num += 2 ** m  # handle negative numbers
    binary = convert_to_binary(num, m)
    result[i] = binary

print(result)
```

Output:
```
[[0 0 0 0 0 1]
 [0 0 0 0 1 0]
 [0 0 0 0 1 1]
 [0 0 0 1 0 0]
 [0 0 0 1 0 1]]
```

This solution first converts each integer to a binary numpy array using `np.unpackbits()`. Then, it selects the last `m` bits from the binary array using slicing. If the number is negative, it adds `2 ** m` to it to handle overflow.

Finally, the result is a 2D numpy array where each row represents the binary representation of the corresponding integer in `a`.