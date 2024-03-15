from collections import Counter

def count_views_by_user(df, bins):
	df['counts'] = df['views'].groupby('username').sum()
	return df[df['counts'].sum()].sort_values(by='counts', ascending=False).reset_index(drop=True)
