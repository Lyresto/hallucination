def y_over_x(y,x):
	return sum(y[i] - x[i] for i in range(len(x))) / len(x)

df = pd.DataFrame({'x':x, 'y':y})
plt.plot(df['y'], df['x'])
plt.legend(df['y'], df['x'], loc='upper right')

print(df.plot(x='y'))
