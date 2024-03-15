from itertools import zip_longest

def add(df, col):
	for i in df:
		df[col] += i[1]
	return df

def col_to_rgb(col_name):
	rgb = {i: (j // 255, j % 255) for i, j in zip_longest(*[iter(col_name)] * 3)}
	return tuple(rgb[i] for i in range(3))
	
df = pd.DataFrame(data=y)
ax = df.plot(x='X', y='Y')

# make both the x and y axis tick labels red
ax = add(df, 'X')
ax = add(df, 'Y')
ax = col_to_rgb(ax)

# SOLUTION END
