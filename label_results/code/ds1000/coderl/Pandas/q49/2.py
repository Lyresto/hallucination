import pandas as pd

def df_average(df, section_left, section_right):
	lis = df.index.values
	n = len(lis)
	lis = [i for i in lis if i < section_left and i > section_right]
	result = sum(df.loc[i]['value'] for i in lis) / len(lis)
	for i in range(section_left, section_right):
		result += df.loc[i]['value']
	return result
