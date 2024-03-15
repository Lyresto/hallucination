from pandas import datetime

def time_to_num(s):
	return int(datetime.strptime(s, '%Y-%m-%d %H:%M:%S').timestamp())

def rank_df(df):
	ranks = df.groupby('ID')['TIME'].rank(ascending=False)
	return ranks
