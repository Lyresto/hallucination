import pandas as pd

def val_columns_generator(n):
	def generator():
		for i in range(n):
			yield i, i+1
	return generator()

def sum_columns(df, n):
	return sum(df[col].sum() for col in val_columns_generator(n))

df = pd.DataFrame({'group': ['A', 'A', 'A', 'B', 'B'], 'group_color' : ['green', 'green', 'green', 'blue', 'blue'], 'val1': [5, 2, 3, 4, 5], 'val2' : [4, 2, 8, 5, 7], 'val3': [1,1,4,5,1], 'val4': [2,2,3,4,5]})
print((sum_columns(df, 3)))
