from datetime import datetime

def rank_df(df):
	ranks = {}
	for _, row in df.iterrows():
		times = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in row['TIME']]
		ranks[row['ID']] = times.count(min(times))
	return ranks
