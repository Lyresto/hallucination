last_column = df.columns[-1]
df.rename(columns={last_column: 'Test'}, inplace=True)
result = df
