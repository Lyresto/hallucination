df['Q_cum'] = df.groupby('D')['Q'].cumsum()
