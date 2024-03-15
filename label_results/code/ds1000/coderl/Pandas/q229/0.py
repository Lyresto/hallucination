from collections import defaultdict
from itertools import groupby

def count_views_in_bins(df, bins):
	counts = defaultdict(lambda: 0)
	for u, g in groupby(df.copy(), key='post_id'):
		counts[u] += g.count()
	return sum(counts[u] for u in counts)
