import numpy as np
#import scipy.ndimage
#f = scipy.ndimage.convolve(np.reshape(x, (2, 2)), np.reshape(y, (2, 2)),'same')
#f = scipy.ndimage.convolve(np.reshape(x, (2, 2)), np.reshape(y, (2, 2)),'same')


from scipy.ndimage import convolve, smoothing
#f = smoothing(f, mode='same')

fig, ax = plt.subplots()
ax.scatter(x, y, s=20, c='r')
ax.scatter(x, y, s=20, c='b')
ax.set_ylim(-20, 20)
ax.set_xlim(-20, 20)

fig.tight_layout()
