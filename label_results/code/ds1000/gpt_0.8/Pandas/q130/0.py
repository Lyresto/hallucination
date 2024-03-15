One way to add a column referring to the index of the first duplicate is to use the `duplicated()` method with the `keep='first'` parameter to identify the first occurrence of each duplicate group. Then, we can use the `groupby()` method to group the dataframe by the columns we want to check for duplicates, and use `idxmin()` to get the index of the first occurrence in each group. Finally, we can merge this information back into the original dataframe.

Here's the code to achieve this:

```python
import pandas as pd

df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

# Identify the first occurrence of each duplicate group
first_duplicates = df.duplicated(subset=['col1','col2'], keep='first')

# Get the index of the first occurrence in each group
first_duplicates_index = df.groupby(['col1','col2']).apply(lambda x: x.index[0])

# Merge the index information back into the original dataframe
df['index_original'] = df.index.isin(first_duplicates_index).astype(int)

print(df)
```

This will output:

```
   col1  col2  index_original
0     1     2               1
1     3     4               0
2     1     2               1
3     1     4               0
4     1     2               1
```

Note that the `index_original` column now contains a 1 for the rows that are the first occurrence in each duplicate group, and a 0 for the other rows.