One way to achieve this is by using the `concat` function from the `pandas` library along with the `apply` method. Here's an example:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])

dataframes = [a, b, c]

result = pd.concat(dataframes, axis=1).apply(tuple, axis=1).to_frame()
result.columns = ['one', 'two', 'three']
```

This code creates a list `dataframes` containing all the dataframes you want to concatenate. Then, the `concat` function is used to concatenate them along the columns (`axis=1`). The `apply` method with `tuple` as the function argument is used to convert each row of the concatenated dataframe into a tuple. Finally, the result is converted into a dataframe using `to_frame()` and the columns are renamed accordingly.

You can easily extend this solution to accommodate an arbitrary number of dataframes by simply adding them to the `dataframes` list.