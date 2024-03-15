le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
transformed_df = df
