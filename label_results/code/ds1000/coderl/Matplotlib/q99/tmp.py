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

# Make a scatter plot with x and y and remove the edge of the marker
# Use vertical line hatch for the marker
# SOLUTION START



def scatter_plot(x, y, color='r', marker='.'):
    # scatter_plot(x, y, color=color, marker='D')
    # scatter_plot(x, y, marker='^', color=color)
    # scatter_plot(x, y, marker='*', color=color)
    
    p = pd.Series([x, y], index=x)
    p.plot(marker=marker, color=color, lw=2)
    
    return p.plot(color=color)

# make a scatter plot with x and y and remove the edge of the marker.
# Use vertical line hatch to mark the marker

# SOLUTION START
import numpy as np

x = np.arange(10)
y = np.arange(10)
c = np.array([1,1,2,2,3])

p = scatter_plot(x, y, c, 'D')

# p = scatter_plot(x, y, c, 'x')
# p = scatter_plot(x, y, c, 'y')

# p = scatter_plot(x, y, c, '.')
# p = scatter_plot(x, y, c, '*')

# p = scatter_plot(x, y, c, 'r')
# p = scatter_plot(x, y, c, 'y')

# p = scatter_plot(x, y, c, '.')
# p = scatter_plot(x, y, c, 'x^')

# p = scatter_plot(x, y, c, '^')

# p = scatter_plot(x, y, c, 'D')

# p = scatter_plot(x, y, c, '^')



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
ax = plt.gca()
lw_flag = True
for l in ax.collections[0].get_linewidth():
    if l != 0:
        lw_flag = False

assert lw_flag
assert ax.collections[0].get_hatch() is not None
assert "|" in ax.collections[0].get_hatch()[0]
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
