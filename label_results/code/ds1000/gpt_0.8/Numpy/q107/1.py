One way to compute the series B is to use a for loop and iterate over the values of A. Here's an example implementation using pandas and numpy:

```python
import numpy as np
import pandas as pd

A = pd.Series(np.random.randn(10,))
a = 2
b = 3

B = pd.Series(index=A.index)

B[0] = a * A[0]

for t in range(1, len(A)):
    B[t] = a * A[t] + b * B[t-1]

print(B)
```

This will give you the desired series B. Note that we initialize B as an empty series with the same index as A, and then fill in each element using the recursive formula.