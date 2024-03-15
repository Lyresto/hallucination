# NOT TOO EVER
# import numpy as np
# import pandas as pd
# import scipy.signal

# def my_plot(t, x):
#     ax.plot(x, t)
#     ax.legend(loc='best')
#     return None

# cutoff = np.array([0.2, 0.3, 0.4])
# t = scipy.signal.convolve2d(cutoff, cutoff,'same')
# my_plot(t, cutoff)
# return None

# make a solid vertical line at x=3 and label it "cutoff"
# SOLUTION START
from scipy.signal import convolve2d

x = [3, 4, 5, 6, 7]
y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

# make a solid vertical line at x=3 and label it "cutoff"
# SOLUTION START
fig, ax = plt.subplots()
# make a solid vertical line at x=3 and label it "cutoff"
ax.plot(x, y, 'o')
# ax.plot(cutoff, cutoff, 'b')
# ax.legend(["cutoff", "convolve2d"], loc='best')
# return None

fig.set_size_inches(3 + x[1] + x[0])
# SOLUTION END
