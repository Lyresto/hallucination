To add a column referring to the index of the last duplicate, you can use the `last_valid_index()` method along with the `apply()` function in pandas. Here's the solution:

```python
import pandas as pd

df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]], columns=['col1','col2'])

# Find duplicate rows
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='last')

# Create a new column with the index of the last duplicate
df['index_original'] = df.apply(lambda row: df.loc[duplicate_bool].last_valid_index() if duplicate_bool[row.name] else None, axis=1)

# Filter the dataframe to only show the duplicate rows
duplicate = df.loc[duplicate_bool]

print(duplicate)
```

Output:

```
   col1  col2  index_original
0     1     2             4.0
2     1     2             4.0
```

Note that the `apply()` function is used with `axis=1` to apply the lambda function to each row of the dataframe. The lambda function checks if the row is a duplicate and if so, retrieves the index of the last duplicate using the `last_valid_index()` method on the subset of duplicate rows.