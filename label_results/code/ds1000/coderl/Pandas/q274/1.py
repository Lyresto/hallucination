import numpy as np
from pandas import DataFrame

def average(list_of_my_columns):
	my_list = []
	for i in list_of_my_columns:
		my_list.append(DataFrame[i])
	for i in range(len(my_list)):
		my_list[i]['Avg'] = np.mean(my_list[i])
	return my_list[0]
