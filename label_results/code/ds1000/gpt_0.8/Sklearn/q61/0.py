One possible solution to convert the features to a 2D-array using sklearn and numpy is as follows:

```python
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

features = [
    ['f1', 'f2', 'f3'],
    ['f2', 'f4', 'f5', 'f6'],
    ['f1', 'f2']
]

def solve(features):
    mlb = MultiLabelBinarizer()
    new_features = mlb.fit_transform(features)
    return new_features

new_features = solve(features)
print(new_features)
```

Output:
```
[[1 1 1 0 0 0]
 [0 1 0 1 1 1]
 [1 1 0 0 0 0]]
```

In this solution, we first import the necessary libraries - numpy and sklearn's MultiLabelBinarizer. Then, we define a function `solve` which takes in the list of features as an input.

Inside the `solve` function, we create an instance of the MultiLabelBinarizer class `mlb`. This class is used to transform the list of features into a binary matrix representation. We then call the `fit_transform` method of `mlb` to convert the features into a 2D-array `new_features`.

Finally, we return the `new_features` array as the solution.