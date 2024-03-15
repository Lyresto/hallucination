from datetime import datetime
import numpy as np

def pivot_table(df, pivot_cols='user', index=0):
    
	if pivot_cols == 'user':
		return df
	
	if len(pivot_cols)!= len(df):
		return None
		
	p_cols = [datetime.strptime(x,'%Y/%m/%d') for x in pivot_cols]
	p_cols = np.array(p_cols, dtype='O')
	pivot_cols = df[pivot_cols]
	pivot_cols = pivot_cols.astype('O')
	
	pivot_rows = pivot_cols.copy()
	for i in range(len(pivot_cols)):
		pivot_rows[i] = pivot_cols[i].pivot(index=index, columns='user')
		
	return pd.concat(pivot_rows, axis=1)
