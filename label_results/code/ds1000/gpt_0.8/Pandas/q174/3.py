df = pd.DataFrame({'index': s.index, '1': s.values})
df = df.sort_values(by=['1', 'index'])
df