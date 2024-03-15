One way to solve this problem is by using a for loop to iterate through the elements of series A and compute the corresponding values of series B. Here's an example of how you can do this using pandas:

```python
import pandas as pd

# Define series A and constants a and b
A = pd.Series(np.random.randn(10,))
a = 2
b = 3

# Compute series B
B = pd.Series(index=A.index)  # Create an empty series B with the same index as A
B[0] = a * A[0]  # Compute the first element of B

for t in range(1, len(A)):
    B[t] = a * A[t] + b * B[t-1]  # Compute the remaining elements of B using the recursive formula

print(B)
```

This will give you a series B that satisfies the recursive formula you provided.