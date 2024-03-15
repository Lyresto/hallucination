To map the values in the dictionary to the 'Date' column in the DataFrame based on the 'Member' column, you can use the `map()` function along with a lambda function. Here's the solution:

```python
import pandas as pd
import numpy as np

example_dict = {'abc':'1/2/2003', 'def':'1/5/2017', 'ghi':'4/10/2013'}
example_df = pd.DataFrame({'Member':['xyz', 'uvw', 'abc', 'def', 'ghi'], 'Group':['A', 'B', 'A', 'B', 'B'], 'Date':[np.nan, np.nan, np.nan, np.nan, np.nan]})

def f(dict=example_dict, df=example_df):
    df['Date'] = df['Member'].map(lambda x: dict.get(x, np.nan))
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

In this solution, we use the `map()` function to apply a lambda function to each value in the 'Member' column. The lambda function looks up the value in the dictionary using `dict.get(x, np.nan)`, which returns the value from the dictionary if it exists, or `np.nan` if it doesn't. We assign the result of this mapping to the 'Date' column in the DataFrame.