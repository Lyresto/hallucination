from scipy import stats
def column_zscore(df):
	xs = [float(i) for i in df.probegenes]
	return (stats.scoreatpercentile(xs, 80)).round(2), (stats.scoreatpercentile(xs, 90)).round(2)
