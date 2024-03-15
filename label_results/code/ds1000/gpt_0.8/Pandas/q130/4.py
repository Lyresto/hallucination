import pandas as pd

df=pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

df['index_original'] = df.duplicated(subset=['col1','col2'], keep='first').astype(int).cumsum()
duplicate = df[df.duplicated(subset=['col1','col2'], keep='first')]
duplicate