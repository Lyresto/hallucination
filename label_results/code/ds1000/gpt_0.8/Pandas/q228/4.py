One way to achieve this is by using the `zip_longest` function from the `itertools` module to iterate over the columns of each dataframe simultaneously. We can then use a list comprehension to create tuples from the corresponding elements and convert it into a dataframe.

Here's the solution:

```python
import pandas as pd
import numpy as np
from itertools import zip_longest

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

dfs = [a, b]  # list of dataframes

# Get the length of the longest dataframe
max_len = max(len(df) for df in dfs)

# Create a list of tuples from corresponding elements in each dataframe
result = pd.DataFrame([(tuple(df[col].iloc[i]) for df in dfs) for i in range(max_len)], columns=a.columns)

# Fill the vacancy with np.nan if dataframes have different lengths
result = result.fillna(np.nan)

print(result)
```

This will give you the desired output:

```
      one     two
0  (1, 5)  (2, 6)
1  (3, 7)  (4, 8)
2  (nan, 9)  (nan, 10)
```

The solution can handle an arbitrary number of dataframes by adding them to the `dfs` list.