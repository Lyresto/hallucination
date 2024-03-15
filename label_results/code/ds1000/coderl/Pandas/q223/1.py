from math import ceil
def fillna(df, x='column_x'):
	fill_value = df[x].mode()[0]
	if fill_value == 0:
		return df[x].fillna(0)
	else:
		fill_value = ceil(fill_value*100/16000)
		return df[x].fillna(fill_value)
