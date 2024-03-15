def df_without_nans():
	import numpy as np
	import pandas as pd
	index = ['x', 'y']
	columns = ['a','b','c']
	df = pd.DataFrame(data=np.zeros((2,3), dtype='int32,float32'), index=index, columns=columns)
	df.values.dtype
	return df

def df_with_nans():
	import numpy as np
	index = ['x', 'y']
	columns = ['a','b','c']
	df = pd.DataFrame(data=np.zeros((2,3), dtype='int32,float32'), index=index, columns=columns)
	df.values.dtype
	return df2
