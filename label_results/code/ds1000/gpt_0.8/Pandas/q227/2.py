One way to achieve this is by using the `zip` function in combination with a list comprehension. Here's an example of how you can create the desired dataframe:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])

dfs = [a, b, c]
columns = a.columns

result = pd.DataFrame([[tuple(row[column] for row in df.itertuples(index=False)) for df in dfs] for column in columns], columns=columns)
```

In this code, we define a list `dfs` containing all the dataframes `a`, `b`, `c`. We also store the column names of `a` in the variable `columns`.

Then, using a list comprehension, we iterate over each column in `columns` and create a list of tuples. Each tuple is formed by taking the corresponding elements from each dataframe in `dfs` using a nested list comprehension and the `itertuples` method.

Finally, we create a new dataframe `result` using the list of tuples as the data and the `columns` variable as the column names.

Note that this solution assumes that all the dataframes have the same shape and column names.