from pandas import DataFrame
from numpy import where

def check_columns(df1, df2):
	check = [df1[column]!= df2[column] for column in df1.columns if column in df2.columns]
	return list(where(check))
