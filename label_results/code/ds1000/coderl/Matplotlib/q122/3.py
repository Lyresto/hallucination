import pandas as pd

df = pd.DataFrame({'x':x, 'y':y})
df['z'] = df['x'] + df['y']

# Adjust the length of the legend handle to 0.3
legend = df.plot(y="z", x="x")
legend.set_size(0.3)

# SAVE THE MOVE TO A FILE
plt.savefig('line.png')
