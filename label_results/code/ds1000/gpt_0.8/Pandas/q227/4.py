To create a dataframe `a_b_c` containing tuples from the series of dataframes `a`, `b`, and `c`, you can use the `zip()` function along with a list comprehension. Here's how you can do it:

```python
import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])

df_list = [a, b, c]
a_b_c = pd.DataFrame([(x, y, z) for x, y, z in zip(*[df.values.tolist() for df in df_list])], columns=df_list[0].columns)
```

The above code will create a new dataframe `a_b_c` containing tuples formed from the corresponding elements in `a`, `b`, and `c`. You can also extend this solution to an arbitrary number of dataframes by including them in the `df_list` list.