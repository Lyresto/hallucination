from itertools import groupby

def get_rows(df):
	return list(filter(lambda r: min(r['count']) == min(r[c] for c in 'S1') for _,r in groupby(df, 'Sp'))
