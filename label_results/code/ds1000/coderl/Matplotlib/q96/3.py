# SOLUTION START


df = pd.DataFrame({'x': x, 'y': y})

for i in range(2):
	df['y'] = df.y.apply(lambda r: r + i * y)
	
df.plot.bar()

plt.title('Figure')

# # SOLUTION END
