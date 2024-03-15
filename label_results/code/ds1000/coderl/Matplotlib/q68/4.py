import pandas as pd

df = pd.DataFrame({'x': x, 'y': y})
df = df.plot(x='x', y='y')

plt.gca().set_title('y over x')

print(df.legend())
