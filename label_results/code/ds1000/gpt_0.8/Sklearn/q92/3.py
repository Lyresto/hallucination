transformed_df = df.copy()
le = LabelEncoder()
transformed_df['Sex'] = le.fit_transform(transformed_df['Sex'])
