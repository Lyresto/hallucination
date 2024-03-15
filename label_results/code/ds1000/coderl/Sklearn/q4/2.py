import pandas as pd
import numpy as np
import sklearn

def one_hot_encode(list):
	return list.map(lambda x: 1 if x in x.split() else 0)
	
def load_data():
	df = pd.DataFrame.from_dict({i:[] for i in range(1,len(df)+1)})
	for i in df:
		df[i] = one_hot_encode(df[i])
	return df
	
		
