import numpy as np

x = np.arange(10)
y = np.arange(10)
s1 = np.square(x)
s2 = np.square(y)

df = pd.DataFrame({'x':x, 'y':y})

# make a line plot with all points
df['y'].plot(kind = 'line', color ='red')

# make legend
df['y'].plot(kind = 'legend', fontsize = 8)

# make a grid of points
grid = np.arange(10).reshape(4, 4)
df['x'].plot(kind = 'grid', color = 'black', grid = grid)

# make legend
df['y'].plot(kind = 'legend', fontsize = 8)

# make grid
grid = np.arange(10).reshape(4, 4)
df['x'].plot(kind = 'grid', color = 'green', grid = grid)

# make grid
grid = np.arange(10).reshape(4, 4)
df['y'].plot(kind = 'grid', color = 'blue', grid = grid)


# SOLUTION END
