import numpy as np
import pandas as pd

np.random.seed(10)
data = {}
for i in [chr(x) for x in range(65,91)]:
	data['Col '+i] = np.random.randint(1,100,10)
df = pd.DataFrame(data)
list_of_my_columns = ['Col A', 'Col E', 'Col Z']
avg_list_of_my_columns = np.array(list_of_my_columns)
for i in range(len(list_of_my_columns)):
	df['Avg'] = df[list_of_my_columns].mean(axis=1)


