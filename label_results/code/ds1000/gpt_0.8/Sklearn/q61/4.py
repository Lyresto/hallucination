One possible solution is to use the `MultiLabelBinarizer` class from the `sklearn.preprocessing` module. This class can be used to binarize multiple labels into a one-hot encoded array.

Here's an example of how you can use it to transform your list of features into a 2D array:

```python
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

features = [
    ['f1', 'f2', 'f3'],
    ['f2', 'f4', 'f5', 'f6'],
    ['f1', 'f2']
]

mlb = MultiLabelBinarizer()
new_features = mlb.fit_transform(features)
```

The resulting `new_features` array will be:

```
array([[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0, 0]])
```

Each row of the array corresponds to a sample, and each column corresponds to a unique feature. The value in each cell represents whether the feature is present (1) or not (0) for that particular sample.

Note that the `MultiLabelBinarizer` class expects the input features to be in a list of sets format, so you may need to preprocess your data accordingly if it is not already in this format.