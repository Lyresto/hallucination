df = pd.DataFrame({'X': x, 'Y': y})
ax = df.plot(x='X', y='Y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
