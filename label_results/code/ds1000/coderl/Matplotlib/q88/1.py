# SOLUTION END
import numpy as np
df = pd.DataFrame({"x": np.arange(10), "y": np.arange(10)})
df.plot(x="x", y="y")
