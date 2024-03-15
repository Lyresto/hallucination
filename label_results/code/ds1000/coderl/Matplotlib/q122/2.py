# SOLUTION START
import numpy as np
import pandas as pd

# plot y over x with a legend of "Line"
# Adjust the length of the legend handle to be 0.3
# SOLUTION START
x = np.arange(10)
y = np.arange(10)
df = pd.DataFrame({"x":x,"y":y})
ax = df.plot(legend=True,fontsize=0.3)

# ALWAYS CHANGED

# Adjust the length of the legend handle to be 0.3
# SOLUTION START
