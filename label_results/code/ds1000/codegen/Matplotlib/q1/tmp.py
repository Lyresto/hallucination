import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y)

# how to turn on minor ticks on y axis only
# SOLUTION START
plt.yticks(np.arange(0, 1.1, 0.1))
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
# x axis has no minor ticks
# y axis has minor ticks
ax = plt.gca()
assert len(ax.collections) == 1
xticks = ax.xaxis.get_minor_ticks()
for t in xticks:
    assert not t.tick1line.get_visible()

yticks = ax.yaxis.get_minor_ticks()
assert len(yticks) > 0
for t in yticks:
    assert t.tick1line.get_visible()
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
