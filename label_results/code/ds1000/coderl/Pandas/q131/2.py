import pandas as pd

df = pd.DataFrame(data=[[1,2],[3,4],[1,2],[1,4],[1,2]],columns=['col1','col2'])

def find_duplicate_cols(df):
	col_list = df.columns.values.tolist()
	dup_bool = df.duplicated(subset=col_list, keep='last')
	dup_cols = df.loc[dup_bool]
	return dup_cols
	
def duplicate_column_with_index(df,col_name):
	col_list = df.columns.values.tolist()
	dup_bool = df.duplicated(subset=col_list, keep='last')
	dup_cols = df.loc[dup_bool]
	new_col_names = [c for c,v in enumerate(col_list) if v == col_name]
	return dup_cols.append(pd.Series(new_col_names,name=col_name))
