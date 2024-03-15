import pandas as pd
df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])
df_dups = df.duplicated(subset=['col1','col2'], keep='first')
print(df_dups)
