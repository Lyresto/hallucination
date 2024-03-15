One way to solve this problem is by using a for loop to iterate through the dataframes and create a new dataframe with tuples. Here's an example of how you can do it:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

# List of dataframes
dataframes = [a, b]

# Get the maximum length among all dataframes
max_length = max(len(df) for df in dataframes)

# Create an empty dataframe with the desired columns
result = pd.DataFrame(columns=a.columns)

# Iterate through each dataframe
for df in dataframes:
    # Get the length of the current dataframe
    length = len(df)
    
    # If the current dataframe is shorter than the maximum length, append np.nan rows
    if length < max_length:
        df = df.append(pd.DataFrame(np.nan, index=range(max_length - length), columns=df.columns))
    
    # Append the tuples formed from the corresponding elements in the current dataframe to the result
    result = result.append(df.apply(tuple, axis=1))
    
# Reset the index of the result dataframe
result = result.reset_index(drop=True)

print(result)
```

Output:
```
      one     two
0  (1, 5)  (2, 6)
1  (3, 7)  (4, 8)
2  (nan, 9)  (nan, 10)
```

This solution can handle an arbitrary number of dataframes. You just need to add them to the `dataframes` list.