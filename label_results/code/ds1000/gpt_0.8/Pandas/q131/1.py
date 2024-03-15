import pandas as pd

df=pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

# Find duplicate rows
duplicate_bool = df.duplicated(subset=['col1','col2'], keep='last')
duplicate = df.loc[duplicate_bool == True]

# Add a column for the index of the last duplicate
duplicate['index_original'] = df[duplicate_bool == True].index[-1]

# Print the final result
print(duplicate)
