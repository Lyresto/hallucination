One way to solve this problem is to group the data by column 'a', calculate the mean and standard deviation of column 'b' for each group, and then create a new dataframe with the results. Here's one way to do it:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':[1,1,1,2,2,2,3,3,3], 'b':[12,13,23,22,23,24,30,35,55]})

grouped = df.groupby('a')['b']  # Group the data by column 'a'
mean_std = grouped.agg(['mean', 'std'])  # Calculate mean and standard deviation of column 'b' for each group
mean_std.columns = ['mean', 'std']  # Rename the columns
mean_std = mean_std.reset_index()  # Reset the index

print(mean_std)
```

Output:
```
   a  mean        std
0  1  16.0   6.082763
1  2  23.0   1.000000
2  3  40.0  13.228757
```

The `groupby` function groups the data by column 'a'. The `agg` function is used to calculate the mean and standard deviation of column 'b' for each group. The resulting dataframe is then assigned column names 'mean' and 'std' using the `columns` attribute. Finally, the index is reset using the `reset_index` function to obtain the desired output format.