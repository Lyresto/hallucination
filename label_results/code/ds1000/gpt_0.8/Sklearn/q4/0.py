from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
df_out = pd.concat([df, pd.DataFrame(mlb.fit_transform(df['Col3']), columns=mlb.classes_)], axis=1).drop('Col3', axis=1)
