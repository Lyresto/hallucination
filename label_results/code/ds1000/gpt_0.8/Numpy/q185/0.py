df = pd.DataFrame(data)
df['Q_cum'] = df.groupby('D')['Q'].cumsum()
df