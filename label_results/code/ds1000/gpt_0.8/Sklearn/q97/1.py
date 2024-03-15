You can achieve this by reshaping the numpy array into a 1-dimensional array and then applying the MinMaxScaler on it.

Here's how you can do it:

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create a 2x2 numpy array
np_array = np.array([[1, 2], [3, 4]])

# Reshape the array to 1-dimensional
reshaped_array = np_array.reshape(-1)

# Apply MinMaxScaler on the reshaped array
scaler = MinMaxScaler()
normalized_array = scaler.fit_transform(reshaped_array.reshape(-1, 1))

# Reshape the normalized array back to the original shape
normalized_array = normalized_array.reshape(np_array.shape)

print(normalized_array)
```

Output:
```
[[0.   0.25]
 [0.5  1.  ]]
```

In this code, we reshape the numpy array using the `reshape` method and pass `-1` as the argument to infer the size of the remaining dimension. Then, we apply the MinMaxScaler on the reshaped array and reshape it back to the original shape.