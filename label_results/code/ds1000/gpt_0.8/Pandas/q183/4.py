To map the values in the dictionary to the "Date" column in the DataFrame based on the matching keys in the "Member" column, you can use the `map` function along with the `fillna` function to preserve the values in the "Date" column that do not have a corresponding key in the dictionary.

Here is the solution:

```python
import pandas as pd
import numpy as np

# Example dictionary
example_dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}

# Example DataFrame
example_df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

# Function to map values from dictionary to DataFrame
def f(dict=example_dict, df=example_df):
    # Map values from dictionary to "Member" column and fill NaN values with original values
    df['Date'] = df['Member'].map(dict).fillna(df['Date'])
    return df

# Call the function
result = f()
print(result)
```

Output:
```
  Member Group        Date
0    xyz     A         NaN
1    uvw     B         NaN
2    abc     A  1/2/2003
3    def     B  1/5/2017
4    ghi     B  4/10/2013
```

The `map` function is used to replace the values in the "Member" column with the corresponding values from the dictionary. The `fillna` function is then used to fill NaN values in the "Date" column with the original values.

Note: It is recommended not to use `dict` as a variable name as it is a built-in Python keyword. In the example above, I used `example_dict` instead.