To map the values in the dictionary to the "Date" column in the DataFrame based on the key values, you can use the `map` function along with the `fillna` function to preserve the values that do not have a corresponding key in the dictionary.

Here's the solution:

```python
import pandas as pd
import numpy as np

# Given dictionary
example_dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}

# Given DataFrame
example_df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

# Map the values from the dictionary to the "Date" column based on the key values
example_df['Date'] = example_df['Member'].map(example_dict).fillna(example_df['Date'])

# Print the updated DataFrame
print(example_df)
```

Output:
```
  Member Group        Date
0    xyz     A         NaN
1    uvw     B         NaN
2    abc     A   1/2/2003
3    def     B   1/5/2017
4    ghi     B  4/10/2013
```

This code uses the `map` function to map the values from the dictionary to the "Member" column in the DataFrame. Then, the `fillna` function is used to fill the NaN values in the "Date" column with the corresponding values from the "Member" column. The final result is stored back in the "Date" column of the DataFrame.