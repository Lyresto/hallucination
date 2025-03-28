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

# make a two columns and one row subplots. Plot y over x in each subplot.
# Give the plot a global title "Figure"
# SOLUTION START
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Figure")

axs[0].plot(x, y)
axs[0].set_title("Subplot 1")

axs[1].plot(x, y)
axs[1].set_title("Subplot 2")




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
assert f.axes[0].get_gridspec().ncols == 2
assert f.axes[0].get_gridspec().nrows == 1
assert f._suptitle.get_text() == "Figure"
for ax in f.axes:
    assert ax.get_title() == ""
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
