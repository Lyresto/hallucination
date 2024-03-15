import numpy as np
from pandas import DataFrame

def __starting_point():
	df = DataFrame({'A': [1,1,0,1], 'B': [0,0,0,0], 'C': [1,1,0,1], 'D': [0,1,0,1]})
	ans = np.array([['0','1','1','0'],[0,'1','1','1'],[0,'1','0','0'],[1,1,1,1]])
	print(ans)
	print(df)
	print(df.sum(0))

__starting_point()
