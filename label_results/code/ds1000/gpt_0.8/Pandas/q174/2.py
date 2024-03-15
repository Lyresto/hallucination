df = pd.DataFrame({'index': s.index, 'value': s.values})
df = df.sort_values(by=['value', 'index'], ascending=[True, True])
df