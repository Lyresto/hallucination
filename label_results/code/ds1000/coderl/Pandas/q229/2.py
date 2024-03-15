from collections import Counter

def count_views_in_bins(df, bins):
	counts = dict(Counter(df['username']))
	for bin_size in bins:
		for group in df.groupby(pd.cut(df.views, bin_size)):
			counts[group['username']] += group['views']
	return sum(counts.values())
