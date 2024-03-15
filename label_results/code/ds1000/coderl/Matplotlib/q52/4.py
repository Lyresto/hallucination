import numpy as np

y = np.array(y)
x = np.arange(10)

df = pd.DataFrame({"y": y, "x": x})

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

df["y"] + df["x"]

# move the y axis ticks to the right
ax.set_ybound(0, 10)

# Plot x over y
df["y"].plot(x, y, ax=ax)

# SOLUTION END
