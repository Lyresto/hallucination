def Qcum(df, n):
	if n == 'Q':
		return df['Q_cum'].cumsum()
	else:
		return df[n]
