from statistics import mean
df = pd.DataFrame()
list_of_my_columns = ['Col A', 'Col E', 'Col Z']
for i in range(len(list_of_my_columns)):
	df[list_of_my_columns[i]] = mean(df[list_of_my_columns[i]])
print((df[list_of_my_columns].mean(axis=1)))
