df['Column_x'].fillna(0, inplace=True)
n = df['Column_x'].isnull().sum()
df.loc[df['Column_x'].isnull().head(int(n/2))] = 1
