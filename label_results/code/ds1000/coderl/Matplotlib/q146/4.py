# SOLUTION END

df = pd.DataFrame({'x': x, 'y': y})
df['z'] = df['y'] / df['x']
df.plot.bar(x='x', y='y', alpha=0.5)
df.plot.legend(loc='best')
