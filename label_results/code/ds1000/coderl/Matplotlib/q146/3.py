x = [1,2,3,4,5,6,7,8,9,0]
y = [1,2,3,4,5,6,7,8,9,0]
df = pd.DataFrame({'x':x, 'y':y})
df.plot(x='x', y='y', kind='line')
# make legend fontsize 8
