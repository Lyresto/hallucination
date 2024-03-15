To create a pandas dataframe with the desired format, you can use the `zip` function to iterate over the arrays row-wise, and then create a dataframe from the resulting tuples. Here's the code to do this:

```python
import pandas as pd

lat = np.array([[10, 20, 30],
                [20, 11, 33],
                [21, 20, 10]])
lon = np.array([[100, 102, 103],
                [105, 101, 102],
                [100, 102, 103]])
val = np.array([[17, 2, 11],
                [86, 84, 1],
                [9, 5, 10]])

# Create a list of tuples by zipping the arrays row-wise
data = list(zip(lat.flatten(), lon.flatten(), val.flatten()))

# Create a pandas dataframe from the list of tuples
df = pd.DataFrame(data, columns=['lat', 'lon', 'val'])

print(df)
```

This will give you the following output:

```
   lat  lon  val
0   10  100   17
1   20  102    2
2   30  103   11
3   20  105   86
4   11  101   84
5   33  102    1
6   21  100    9
7   20  102    5
8   10  103   10
```

Note that the order of the values in the dataframe follows the row-wise order of the arrays.