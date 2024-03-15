from statistics import mean

def average(df):
	return mean(df['2005'].apply(int))
