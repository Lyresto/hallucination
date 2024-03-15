import numpy as np
df = pd.DataFrame({'x': x, 'y': y})

x_ls = [i for i in range(1, 10)]
y_ls = [i for i in range(1, 10)]

for i in x_ls:
	for j in y_ls:
		df['x' + str(i)] = df['x' + str(i)].apply(lambda x: x - i)
		df['y' + str(j)] = df['y' + str(j)].apply(lambda y: y - j)

#plt.plot(df['x'].values, df['y'].values)
#plt.plot(x_ls, y_ls, 'ro')

# remove the edges
marker = '*'
ax = df.plot(marker=marker, label='left', linestyle='-')

# remove the edges
ax = df.plot(marker=marker, linestyle='--', label='right')

# use vertical line hatch
ax = df.plot(marker='+', linestyle='-', label='top', y_linewidth=2)

# use horizontal line hatch
ax = df.plot(marker='+', linestyle='--', label='bottom', x_linewidth=2)

# SOLUTION END
