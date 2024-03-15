from datetime import datetime

def state(df, col):
	df['state'] = df[col].map(lambda x: x * 50 if x > 50 else 0)
	df['datetime'] = df['datetime'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
	return df[col].sum()
