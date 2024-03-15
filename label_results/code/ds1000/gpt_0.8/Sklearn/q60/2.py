One way to achieve this is to use the `MultiLabelBinarizer` class from sklearn.preprocessing. Here's how you can do it:

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Create an instance of MultiLabelBinarizer
mlb = MultiLabelBinarizer()

# Fit the MultiLabelBinarizer on the features
mlb.fit(features)

# Transform the features into a binary array
new_features = mlb.transform(features)

# Convert the binary array to a DataFrame for better visualization
new_features = pd.DataFrame(new_features, columns=mlb.classes_)
```

The `MultiLabelBinarizer` class is designed to handle multi-label binarization, which is exactly what we need in this case. It treats each sublist in `features` as a separate sample and each element in the sublist as a separate feature.

Note that this solution assumes that the `features` list contains only unique feature values. If there are duplicates within a sublist or across different sublists, the binarized array will have unexpected results. If duplicates are present, you may need to preprocess the `features` list to remove duplicates before applying the binarization.