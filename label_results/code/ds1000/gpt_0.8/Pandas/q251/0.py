df['code_0'] = df['codes'].apply(lambda x: x[0] if len(x) > 0 else None)
df['code_1'] = df['codes'].apply(lambda x: x[1] if len(x) > 1 else None)
df['code_2'] = df['codes'].apply(lambda x: x[2] if len(x) > 2 else None)
result = df.drop('codes', axis=1)
