# I think this is a dumb way to do it :)

import pandas as pd
import numpy as np

np.random.seed(10)
data = {}
for i in [chr(x) for x in range(65,91)]:
	data['Col '+i] = np.random.randint(1,100,10)
df = pd.DataFrame(data)
list_of_my_columns = ['Col A', 'Col E', 'Col Z']

# df[Avg] = df['Col A'] + df['Col E'] + df['Col Z']

for i in range(len(list_of_my_columns)):
	# df[Avg] = df[list_of_my_columns[i]] / len(list_of_my_columns)
	df[list_of_my_columns[i]] = df[list_of_my_columns[i]].mean()

