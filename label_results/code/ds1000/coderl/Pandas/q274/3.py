import pandas as pd
from statistics import mean
df = pd.DataFrame({'Col '+str(i):np.random.randint(1,100,10) for i in range(65,91)})
list_of_my_columns = ['Col A', 'Col E', 'Col Z']
def solve(df,list_of_my_columns):
	for i in range(len(df)):
		df[str(i+'_Avg')] = mean(df[list_of_my_columns])
	return df
