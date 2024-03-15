duplicate_bool = df.duplicated(subset=['col1','col2'], keep='first')
duplicate = df.loc[duplicate_bool == True]
duplicate['index_original'] = df[duplicate_bool == True].index[0]
result = duplicate
