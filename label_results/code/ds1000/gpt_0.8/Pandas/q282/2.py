result = df.copy()
last_column_name = df.columns[-1]
result.rename(columns={last_column_name: 'Test'}, inplace=True)
