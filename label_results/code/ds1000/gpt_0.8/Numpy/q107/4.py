One way to solve this problem is to use a loop to iterate over the elements of A and compute the corresponding elements of B. Here is an example implementation using pandas:

```
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

This will output the series B that satisfies the given algebraic definition.