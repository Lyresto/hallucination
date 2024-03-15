df = pd.read_csv('data.csv')
df['Sex'] = LabelEncoder.fit_transform(df['Sex'])
