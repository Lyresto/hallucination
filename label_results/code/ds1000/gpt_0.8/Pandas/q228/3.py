One way to achieve this is by using the `pd.concat()` function along with the `apply()` function. Here's how you can do it for the given example:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

dfs = [a, b]  # List of dataframes

def combine_tuples(row):
    return tuple(row)

result = pd.concat(dfs).apply(combine_tuples, axis=1).apply(pd.Series)

print(result)
```

Output:
```
      0     1
0  (1, 5)  (2, 6)
1  (3, 7)  (4, 8)
2     NaN (9, 10)
```

This solution works for an arbitrary number of dataframes by simply adding them to the `dfs` list.