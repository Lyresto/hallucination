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

# plot y over x on a 2 by 2 subplots with a figure size of (15, 15)
# repeat the plot in each subplot
# SOLUTION START
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y)
ax[0, 1].plot(x, y)
ax[1, 0].plot(x, y)
ax[1, 1].plot(x, y)
plt.show()
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
f = plt.gcf()
assert (f.get_size_inches() == (15, 15)).all()
for ax in f.axes:
    assert len(ax.get_lines()) == 1
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
