df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a})

fig, [ax1, ax2] = plt.subplots(2, 1)

for i, val in enumerate(df.values):
	ax1.plot(val['x'], val['y'], 'b-')
	ax2.plot(val['z'], val['a'], 'r-')

ax1.set_title('Y and Z')
ax2.set_title('A')

# SOLUTION END
