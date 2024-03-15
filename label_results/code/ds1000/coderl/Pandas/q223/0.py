from math import ceil

def fillna(df, n = 999):
	for i in range(n):
		df['Column_x'] = df['Column_x'].fillna(df['Column_x'].mode()[0], inplace= True)
