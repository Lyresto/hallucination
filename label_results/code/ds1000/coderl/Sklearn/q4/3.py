import pandas as pd
import numpy as np
import sklearn
df = load_data()
df_out = pd.DataFrame()

for i,j in df.iterrows():
	df_out[i] = pd.Series(list(map(int,j)),dtype = np.int)

for i,j in df_out.iterrows():
	df_out.loc[i,i] = 1
