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
from itertools import cycle




def plot_two_subplots(x, y):
    # make x-axes
    xs = cycle(range(x))
    ys = cycle(y)
    xs = list(xs)
    # make y-axes
    ys = list(ys)
    fig, axs = [], []
    for ax, y in zip(axs, ys):
        ax.plot(y, x, 'b-')
    for ax, x in zip(axs, xs):
        ax.plot(x, y, 'r-')
    for ax, x in zip(axs, xs):
        ax.set_title('Y')
    # make 2-grid
    xs = np.arange(0, x.size)
    ys = [next(ys) for _ in range(xs.size)]
    for ax, y in zip(axs, ys):
        ax.plot(y, x, 'g-')
    for ax, x in zip(axs, xs):
        ax.plot(x, y, 'b-')
    for ax, x in zip(axs, xs):
        ax.set_title('X')
    # make 3-grid
    x = pd.Series(x)
    ys = [next(ys) for _ in range(x.size)]
    for ax, y in zip(axs, ys):
        ax.plot(y, x, 'g-')
    for ax, x in zip(axs, xs):
        ax.plot(x, y, 'b-')
    for ax, x in zip(axs, xs):
        ax.set_title('Y')
    # SOLUTION END
    return fig



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
