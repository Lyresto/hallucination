One possible solution is to use the `zip` function to iterate over the corresponding columns of each dataframe, and then use the `apply` method to create tuples from the values in each row.

Here's an example implementation:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])

dataframes = [a, b, c]

result = pd.DataFrame()
for column in a.columns:
    result[column] = pd.Series(zip(*[df[column] for df in dataframes])).apply(tuple)

print(result)
```

Output:
```
      one         two
0  (1, 5, 9)  (2, 6, 10)
1  (3, 7, 11)  (4, 8, 12)
```

This solution uses a for loop to iterate over the columns of one of the dataframes (in this case, dataframe `a`). It then uses a list comprehension to extract the corresponding column from each dataframe in the `dataframes` list. The `zip` function is used to iterate over the values of each column simultaneously, and the `apply` method is used to create tuples from these values. Finally, the resulting tuples are assigned to the columns of the `result` dataframe.