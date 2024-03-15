import pandas as pd

s = pd.Series(y, index=x)
s.plot.bar(x=0)

plt.title('''
y = x
x = 0
phi = Greek letter

''')

# print(s.plot(ax=s.plot()))
