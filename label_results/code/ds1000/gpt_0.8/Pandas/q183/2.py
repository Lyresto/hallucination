You can use the `map()` function in pandas to achieve this. First, create a new column in the DataFrame to store the mapped values. Then, use the `map()` function with the dictionary to map the values based on the 'Member' column. Finally, use `fillna()` to fill the NaN values with the original 'Member' values.

Here's an example solution:

```python
import pandas as pd
import numpy as np

example_dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}
example_df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

def f(dict=example_dict, df=example_df):
    # Create a new column to store the mapped values
    df['Date_mapped'] = df['Member'].map(dict)
    
    # Fill NaN values with original 'Member' values
    df['Date_mapped'] = df['Date_mapped'].fillna(df['Member'])
    
    return df

result = f(example_dict, example_df)
print(result)
```

Output:
```
  Member Group       Date Date_mapped
0    xyz     A        NaN         xyz
1    uvw     B        NaN         uvw
2    abc     A        NaN    1/2/2003
3    def     B        NaN    1/5/2017
4    ghi     B        NaN   4/10/2013
```

The new column 'Date_mapped' contains the mapped values from the dictionary. The NaN values are filled with the original 'Member' values.