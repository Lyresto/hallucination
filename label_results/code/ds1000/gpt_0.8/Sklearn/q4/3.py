from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
df_out = pd.concat([df[['Col1', 'Col2']], pd.DataFrame(mlb.fit_transform(df['Col3']), columns=mlb.classes_)], axis=1)
