from math import *
def multiply_scores_by_10(df, products):
	c=1
	for p,s in zip(df['product'],df['score']):
		c=c*10**p
	return df.multiply(c)
