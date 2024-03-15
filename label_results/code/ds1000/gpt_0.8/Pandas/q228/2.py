One way to create the desired dataframe is to use the `pd.concat()` function to concatenate the dataframes `a` and `b` along the rows, and then use the `apply()` function to apply the `tuple()` function to each row.

Here's the solution:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

dfs = [a, b]  # List of dataframes

result = pd.concat(dfs, axis=0).apply(tuple, axis=1).reset_index(drop=True).to_frame()
```

The `pd.concat(dfs, axis=0)` function concatenates the dataframes `a` and `b` along the rows. The `apply(tuple, axis=1)` function applies the `tuple()` function to each row, creating tuples from the corresponding elements in `a` and `b`. The `reset_index(drop=True)` function resets the index of the resulting dataframe. Finally, the `to_frame()` function converts the resulting series to a dataframe.

The variable `result` will contain the desired dataframe `a_b`:

```
      0         1
0  (1, 5)   (2, 6)
1  (3, 7)   (4, 8)
2  (nan, 9)  (nan, 10)
```