import pandas as pd

df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

duplicate_bool = df.duplicated(subset=['col1','col2'], keep='first')
duplicate = df.loc[duplicate_bool == True]

for i in range(len(duplicate)):
	print(duplicate.loc[i]['col1'], duplicate.loc[i]['col2'], duplicate.loc[i]['index_original'])
