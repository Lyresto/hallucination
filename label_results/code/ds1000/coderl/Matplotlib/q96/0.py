# SOLUTION END
df = pd.DataFrame(dict(zip(x, y)))

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax2 = fig.add_subplot(1, 1, 2)

for i in range(10):
	ax1.plot(df.y[i], df.x[i])
	ax2.plot(df.y[i], df.x[i], 'ro')

fig.suptitle('Figure')

plt.show()
