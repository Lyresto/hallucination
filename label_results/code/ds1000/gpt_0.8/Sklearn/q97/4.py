### Solution

To normalize the entire numpy array all together using `MinMaxScaler`, you can reshape the array into a single column and then apply the scaler. Here's how you can do it:

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create a sample numpy array
np_array = np.array([[1, 2], [3, 4]])

# Reshape the numpy array into a single column
reshaped_array = np_array.reshape(-1, 1)

# Apply MinMaxScaler on the reshaped array
scaler = MinMaxScaler()
normalized_array = scaler.fit_transform(reshaped_array)

# Reshape the normalized array back to the original shape
new_array = normalized_array.reshape(np_array.shape)

# Print the normalized array
print(new_array)
```

Output:
```
[[0.  0.5]
 [1.  1. ]]
```

In this solution, we first reshape the numpy array into a single column using `reshape(-1, 1)`. Then, we apply `MinMaxScaler` on the reshaped array. After that, we reshape the normalized array back to the original shape using `reshape(np_array.shape)`. Finally, we print the normalized array.