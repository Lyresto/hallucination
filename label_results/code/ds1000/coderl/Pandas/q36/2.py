import pandas as pd
def mean_advance(df,row_list,column_list,axis=0):
	for i in range(len(row_list)):
		df[i] = (df[i] + mean(df[column_list[j]][i] for j in range(len(column_list)))) / (len(row_list) + 1)
	return df
