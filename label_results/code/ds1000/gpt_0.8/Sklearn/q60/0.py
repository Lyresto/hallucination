from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
new_features = mlb.fit_transform(features)
