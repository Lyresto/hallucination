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

# make 4 by 4 subplots with a figure size (5,5)
# in each subplot, plot y over x and show axis tick labels
# give enough spacing between subplots so the tick labels don't overlap
# SOLUTION START
fig, axs = plt.subplots(4, 4, figsize=(5, 5))

for i in range(4):
    for j in range(4):
        axs[i, j].plot(x, y)
        axs[i, j].set_xticks(np.arange(0, 10, 2))
        axs[i, j].set_yticks(np.arange(0, 10, 2))
        axs[i, j].tick_params(axis='both', labelsize=6)
        axs[i, j].set_xlim([0, 9])
        axs[i, j].set_ylim([0, 9])
        plt.subplots_adjust(wspace=0.5, hspace=0.5)





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
assert f.subplotpars.hspace > 0.2
assert f.subplotpars.wspace > 0.2
assert len(f.axes) == 16
for ax in f.axes:
    assert ax.xaxis._major_tick_kw["tick1On"]
    assert ax.xaxis._major_tick_kw["label1On"]
    assert ax.yaxis._major_tick_kw["tick1On"]
    assert ax.yaxis._major_tick_kw["label1On"]
    assert len(ax.get_xticks()) > 0
    assert len(ax.get_yticks()) > 0
    for l in ax.get_xticklabels():
        assert l.get_text() != ""
    for l in ax.get_yticklabels():
        assert l.get_text() != ""
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
