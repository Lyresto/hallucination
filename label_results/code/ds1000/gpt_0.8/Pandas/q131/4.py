import pandas as pd

df=pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='last')
duplicate = df.loc[duplicate_bool == True]
duplicate['index_original'] = duplicate.index
result = duplicate