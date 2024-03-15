result = df.groupby('a').agg({'b': ['mean', 'std']})
result.columns = result.columns.droplevel()
result = result.rename(columns={'mean': 'mean_b', 'std': 'std_b'})
result = result.reset_index()
