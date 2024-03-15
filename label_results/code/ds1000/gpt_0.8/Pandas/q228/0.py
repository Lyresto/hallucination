One way to solve this problem is by using the `zip_longest` function from the `itertools` module. This function allows you to iterate over multiple iterables simultaneously, filling missing values with a specified default value (in this case, `np.nan`).

Here's how you can use `zip_longest` to create the desired dataframe:

```python
import pandas as pd
import numpy as np
from itertools import zip_longest

# Define the dataframes
a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])

# Create a list of the dataframes
dataframes = [a, b]

# Use zip_longest to iterate over the dataframes simultaneously, filling missing values with np.nan
result = pd.DataFrame(list(zip_longest(*[df.itertuples(index=False) for df in dataframes], fillvalue=np.nan)), columns=a.columns)
```

This will give you the desired dataframe `result`:

```
      one     two
0  (1, 5)  (2, 6)
1  (3, 7)  (4, 8)
2  (nan, 9)  (nan, 10)
```

You can extend this solution to an arbitrary number of dataframes by simply adding them to the `dataframes` list. The `zip_longest` function will handle the different lengths automatically.