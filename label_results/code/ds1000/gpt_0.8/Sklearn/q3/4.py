There is no direct method in Pandas to convert a Scikit-learn Bunch object to a Pandas DataFrame. However, you can convert the data manually by following these steps:

1. Access the data and target attributes from the Bunch object using the `.data` and `.target` attributes respectively.
2. Combine the data and target arrays using `np.concatenate()` function.
3. Create a DataFrame using the combined array and assign appropriate column names.

Here is the code to convert the Scikit-learn Bunch object to a Pandas DataFrame:

```python
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()

# Combine data and target arrays
combined_array = np.concatenate((data.data, data.target.reshape(-1,1)), axis=1)

# Create DataFrame with column names
column_names = data.feature_names + ['target']
df = pd.DataFrame(combined_array, columns=column_names)

print(df.head())
```

Output:
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                5.1               3.5                1.4               0.2     0.0
1                4.9               3.0                1.4               0.2     0.0
2                4.7               3.2                1.3               0.2     0.0
3                4.6               3.1                1.5               0.2     0.0
4                5.0               3.6                1.4               0.2     0.0
```

In this code, we first concatenate the `data.data` and `data.target` arrays using `np.concatenate()`. Then, we create a DataFrame from the combined array with column names obtained from `data.feature_names` and 'target'. Finally, we print the first few rows of the DataFrame using `df.head()`.