import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import matplotlib.pyplot as plt

H = np.random.randn(10, 10)

# show the 2d array H in black and white
# SOLUTION START
plt.imshow(H, cmap='gray', interpolation='nearest')
plt.colorbar()




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

ax = plt.gca()
assert len(ax.images) == 1
assert isinstance(ax.images[0].cmap, matplotlib.colors.LinearSegmentedColormap)
assert ax.images[0].cmap.name == "gray"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
