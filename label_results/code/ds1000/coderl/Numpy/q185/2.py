def qcumsum(df,name):
	if name == 'Q_cum':
		return df.Q_cum
	else:
		return sum(df[name])
