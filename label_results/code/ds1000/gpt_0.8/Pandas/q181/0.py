df['Date'] = df['Member'].map(dict)
df['Date'] = df['Date'].fillna(df['Member'])
