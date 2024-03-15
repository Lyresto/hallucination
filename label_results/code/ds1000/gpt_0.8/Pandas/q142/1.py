One way to solve this problem in a generalizable way is to use the `pd.melt` function along with some manipulation of the DataFrame columns. Here's an approach you can use:

1. Get the levels of the columns using `df.columns.levels`.
2. Iterate over the levels and create a list of tuples where each tuple represents a set of column levels.
3. Use the list of tuples to set the `value_vars` parameter in `pd.melt`.
4. Reset the column index of the melted DataFrame to remove the original column levels.
5. Rename the melted columns to "variable_0", "variable_1", "variable_2", and "value".

Here's the code to implement this approach:

```python
import pandas as pd

# Step 1: Get the levels of the columns
levels = df.columns.levels

# Step 2: Create a list of tuples for value_vars
value_vars = []
for i in range(len(levels)):
    value_vars.extend([(level[i],) for level in levels])

# Step 3: Use value_vars in pd.melt
melted = pd.melt(df, value_vars=value_vars)

# Step 4: Reset column index
melted = melted.reset_index(drop=True)

# Step 5: Rename melted columns
melted.columns = ['variable_{}'.format(i) if col == 'variable' else col for i, col in enumerate(melted.columns)]

result = melted
```

After running this code, the melted DataFrame will be stored in the `result` variable.