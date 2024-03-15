# SOLUTION END
df = pd.DataFrame({'x': x, 'y': y})
sns.tsplot(df, x='x', y='y', kind='sin')
plt.xlabel('x')
plt.ylabel('y')
