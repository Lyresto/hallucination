from numpy import mean, cov, array, concatenate
from heapq import *

def score_df(df):
	def score(i):
		a, b, c = df.loc[i]
		return mean(a, b, c) + cov(a, b, c)
	h = []
	for i in range(len(df.columns)):
		heappush(h, (-score(i), df.columns[i]))
	return concatenate(h)
