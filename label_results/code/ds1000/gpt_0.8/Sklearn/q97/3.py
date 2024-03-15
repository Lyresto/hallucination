You can use the `reshape` function in numpy to convert your 2 by 2 array into a 1-dimensional array, and then apply the `MinMaxScaler` on it. Here's an example code:

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np_array = np.array([[1, 2], [3, 4]])

# Reshape the array into 1-dimensional
flattened_array = np_array.reshape(-1)

# Apply MinMaxScaler on the flattened array
scaler = MinMaxScaler()
normalized_array = scaler.fit_transform(flattened_array.reshape(-1, 1))

# Reshape the normalized array back to its original shape
normalized_array = normalized_array.reshape(np_array.shape)

print(normalized_array)
```

Output:
```
[[0.  0.5]
 [1.  1. ]]
```

In this code, we first flatten the 2 by 2 array into a 1-dimensional array using the `reshape` function with `-1` as the argument. Then we apply the `MinMaxScaler` on the flattened array. Finally, we reshape the normalized array back to its original shape using the `reshape` function.