from scipy.sparse import csr_matrix
import numpy as np

x = np.arange(10)
y = np.linspace(0, 1, 10)
df = pd.DataFrame({"x":x, "y":y})

matplotlib.use("agg")
matplotlib.pcolormesh(df["x"], df["y"], csr_matrix((np.ones(y.shape) * [0, 1, 0, 1])).T)

# SAVE AND PLOT
plt.show()
