df = pd.DataFrame({'index': s.index, '1': s.values})
df = df.sort_values(by=['1', 'index'], ascending=[True, True])
df.reset_index(drop=True, inplace=True)
df