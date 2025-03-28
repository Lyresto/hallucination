import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.arange(10)

# make two side-by-side subplots and and in each subplot, plot y over x
# Title each subplot as "Y"
# SOLUTION START
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(x, y)
ax[0].set_title('Y')
ax[1].plot(x, y)
ax[1].set_title('Y')
#
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
fig = plt.gcf()
flat_list = fig.axes
assert len(flat_list) == 2
if not isinstance(flat_list, list):
    flat_list = flat_list.flatten()
for ax in flat_list:
    assert ax.get_title() == "Y"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
