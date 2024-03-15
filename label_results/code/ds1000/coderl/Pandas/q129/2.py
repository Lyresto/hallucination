import numpy as np

def fix_dataframe(df):
	#df = df.sample(n)
	print(df)
	new_df = df.copy()
	for i in range(len(df)):
		new_df["UserId"][i] = np.random.randint(len(df["UserId"]) - 1)
		new_df["ProductId"][i] = np.random.randint(len(df["ProductId"]) - 1)
		new_df["Quantity"][i] = np.random.randint(len(df["Quantity"]) - 1)
	return new_df
