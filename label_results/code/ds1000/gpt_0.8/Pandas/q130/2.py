import pandas as pd

df=pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

# Find the duplicate rows
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='first')
duplicate = df.loc[duplicate_bool == True]

# Add a column referring to the index of the first duplicate
duplicate['index_original'] = duplicate.index[0]

result = duplicate

result