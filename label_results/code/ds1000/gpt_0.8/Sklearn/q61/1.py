One way to achieve this is by using the `MultiLabelBinarizer` class from the `sklearn.preprocessing` module. This class can handle the conversion of a list of lists into a binary matrix.

Here's how you can use it:

```python
from sklearn.preprocessing import MultiLabelBinarizer

def solve(features):
    mlb = MultiLabelBinarizer()
    encoded_features = mlb.fit_transform(features)
    new_features = pd.DataFrame(encoded_features, columns=mlb.classes_)
    return new_features

new_features = solve(features)
print(new_features)
```

This will give you the desired 2D-array representation of your features:

```
   f1  f2  f3  f4  f5  f6
0   1   1   1   0   0   0
1   0   1   0   1   1   1
2   1   1   0   0   0   0
```