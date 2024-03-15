One way to achieve this is by using the `map()` function in Pandas. Here's an example of how you can do it:

``` python
import pandas as pd
import numpy as np

example_dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}
example_df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

def f(dict=example_dict, df=example_df):
    df['Date'] = df['Member'].map(dict)
    return df

result = f()
print(result)
```

Output:
```
  Member Group       Date
0    xyz     A        NaN
1    uvw     B        NaN
2    abc     A  1/2/2003
3    def     B  1/5/2017
4    ghi     B  4/10/2013
```

In this code, we use the `map()` function to replace the values in the 'Member' column of the DataFrame with the corresponding values from the dictionary. The `map()` function maps values from the 'Member' column to the values in the dictionary and returns a new Series with the mapped values. We assign this new Series to the 'Date' column of the DataFrame.