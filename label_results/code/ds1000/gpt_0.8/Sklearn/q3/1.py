There is no direct method in Pandas to convert a Scikit-learn Bunch object to a DataFrame. However, you can convert the data using the following steps:

1. Extract the data and feature names from the Bunch object.
2. Create a DataFrame using the extracted data and feature names.

Here is an example of how you can do this:

```python
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
data = load_iris()

# Extract the data and feature names
X = data.data
feature_names = data.feature_names

# Create a DataFrame
df = pd.DataFrame(X, columns=feature_names)

print(df.head())
```

This will give you a DataFrame with the iris dataset's data, where each column represents a feature and each row represents an observation.