One way to achieve this is by using the `MultiLabelBinarizer` class from the `sklearn.preprocessing` module. This class is designed to transform a list of lists (or a list of sets) into a binary matrix.

Here is an example solution using `MultiLabelBinarizer`:

```python
from sklearn.preprocessing import MultiLabelBinarizer

def solve(features):
    mlb = MultiLabelBinarizer()
    transformed_features = mlb.fit_transform(features)
    feature_names = mlb.classes_
    return pd.DataFrame(transformed_features, columns=feature_names)
```

In this solution, we first create an instance of `MultiLabelBinarizer`. We then use the `fit_transform` method to transform the list of lists `features` into a binary matrix. The `fit_transform` method also returns the unique feature names, which we can use as column names when creating a pandas DataFrame.

Note that the returned solution is a pandas DataFrame. If you prefer a numpy array, you can simply convert the DataFrame to a numpy array using the `values` attribute:

```python
return pd.DataFrame(transformed_features, columns=feature_names).values
```

Hope this helps!