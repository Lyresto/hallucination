df = pd.DataFrame({'text': ['abc', 'def', 'ghi', 'jkl']})
df.merge(df, on='text', how='left')
