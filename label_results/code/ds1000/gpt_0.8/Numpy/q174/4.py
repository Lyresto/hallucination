To create a pandas DataFrame with the desired structure, you can use the `zip()` function to iterate over the values in `lat`, `lon`, and `val` simultaneously. Then, you can pass the zipped values to the `pd.DataFrame()` constructor.

Here is an example solution:

```python
import numpy as np
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

def f(lat=lat, lon=lon, val=val):
    # Zip the values of lat, lon, and val
    zipped_values = zip(lat.flatten(), lon.flatten(), val.flatten())
    
    # Create the DataFrame with the zipped values
    df = pd.DataFrame(zipped_values, columns=['lat', 'lon', 'val'])
    
    return df

# Example usage
df = f(lat, lon, val)
print(df)
```

Output:
```
   lat  lon  val
0   10  100   17
1   20  102    2
2   30  103   11
3   20  105   86
...
```

Note that in the example solution, the `flatten()` method is used to flatten the `lat`, `lon`, and `val` arrays. This ensures that the values are iterated over in the correct order.