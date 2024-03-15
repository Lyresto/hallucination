#SOLUTION END
df = pd.DataFrame({'x':x,'y':y})
df['z']=df['y'].mean()
df['z'].plot()
plt.show()
