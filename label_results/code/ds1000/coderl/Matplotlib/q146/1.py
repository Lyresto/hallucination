def f(x, y):
	return (x*y).reshape(x.shape)

df = pd.DataFrame({'x':x, 'y':y})

for i, j in df.iterrows():
	print(i, j)
	f(i, j)
