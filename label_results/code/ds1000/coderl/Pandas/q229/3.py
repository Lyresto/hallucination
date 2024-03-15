from pandas import groupby

def count_views_by_user(df, bins):
	# your code
	df_t = df.copy()
	for key, group in groupby(df_t['post_id'], key = lambda x: x):
		bin_width = max(df_t[key] - 1, bins[0] - 1)
		group_count = sum((df_t[key] // bin_width).values())
		df_t[key] = group_count
	return df_t.username.count()
