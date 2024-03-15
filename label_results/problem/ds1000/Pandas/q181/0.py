df['Date'] = df['Member'].map(dict).fillna(df['Date'])
