import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt
import numpy as np

data = np.random.random((10, 10))

# Set xlim and ylim to be between 0 and 10
# Plot a heatmap of data in the rectangle where right is 5, left is 1, bottom is 1, and top is 4.
# SOLUTION START
from itertools import product




def heatmap(arr):
    xs, ys = list(zip(*arr))
    return plt.pcolormesh(xs, ys, cmap="Greys")



# SOLUTION END
plt.savefig('result/plot.png', bbox_inches ='tight')

#Image Testing
from PIL import Image
import numpy as np
code_img = np.array(Image.open('result/plot.png'))
oracle_img = np.array(Image.open('ans/oracle_plot.png'))
sample_image_stat = (
    code_img.shape == oracle_img.shape
    and np.allclose(code_img, oracle_img)
)
if sample_image_stat:
    with open('result/result_1.pkl', 'wb') as file:
        # if image test passed, we save True to the result file
        pickle.dump(True, file)    
        


# Testing
import matplotlib

for c in plt.gca().get_children():
    if isinstance(c, matplotlib.image.AxesImage):
        break
assert c.get_extent() == [1, 5, 1, 4]
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
