One possible solution is to use the `MultiLabelBinarizer` class from sklearn. Here's how you can achieve it:

```python
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Define the features
features = [
    ['f1', 'f2', 'f3'],
    ['f2', 'f4', 'f5', 'f6'],
    ['f1', 'f2']
]

# Create an instance of the MultiLabelBinarizer
mlb = MultiLabelBinarizer()

# Fit the MultiLabelBinarizer on the features
mlb.fit(features)

# Transform the features into a 2D array
new_features = mlb.transform(features)

# Convert the array to a DataFrame
df = pd.DataFrame(new_features, columns=mlb.classes_)

# Print the result
print(df)
```

This will give you the following output:

```
   f1  f2  f3  f4  f5  f6
0   1   1   1   0   0   0
1   0   1   0   1   1   1
2   1   1   0   0   0   0
```

Note that you need to have scikit-learn installed (`pip install scikit-learn`) in order to use the `MultiLabelBinarizer` class.