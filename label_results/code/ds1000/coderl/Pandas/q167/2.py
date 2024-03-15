from statistics import mean, pstdev

def std_meann(df):
	return pstdev(df.groupby('b').a)
