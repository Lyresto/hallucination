import pandas as pd
#df = pd.read_csv('data.csv')
df = pd.DataFrame({'A_Name': ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG'],
				   'B_Detail': ['X1', 'Y1', 'Z1', 'L1', 'M1', 'N1', 'K1'],
				   'Value_B': [1.2, 0.76, 0.7, 0.9, 1.3, 0.7, -2.4],
				   'Value_C': [0.5, -0.7, -1.3, -0.5, 1.8, -0.8, -0.5],
				   'Value_D': [0.4, 0.5, -0.7, -1.3, 1.8, -0.8, -0.5],
				   'Value_E': [1.3, 1.8, -1.3, 1.8, -1.3, -1.3],
				   'Value_F': [0.7, -0.8, 0.9, 0.7, -0.8, 0.9],
				   'Value_G': [2.4, -1.9, 2.1, -2.4, -1.9, 2.1]})

list1 = []

for i in df.columns:
	if df[i].min()<1:
		list1.append(i)


print(df[list1])
