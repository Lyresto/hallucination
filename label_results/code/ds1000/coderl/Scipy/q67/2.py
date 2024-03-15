from scipy.stats import pstats, mean, median

def zscore(df):
	xs = [mean(df[s]) for s in df.index]
	return pstats.zscore(xs).real
