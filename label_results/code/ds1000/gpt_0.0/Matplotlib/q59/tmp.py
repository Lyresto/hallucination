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

# Plot y over x and label the x axis as "X"
# Make both the x axis ticks and the axis label red
# SOLUTION START
plt.plot(x, y)
plt.xlabel("X", color="red")
plt.xticks(color="red")




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
plt.show()
assert ax.xaxis.label._color in ["red", "r"] or ax.xaxis.label._color == (
    1.0,
    0.0,
    0.0,
    1.0,
)
assert ax.xaxis._major_tick_kw["color"] in ["red", "r"] or ax.xaxis._major_tick_kw[
    "color"
] == (1.0, 0.0, 0.0, 1.0)
assert ax.xaxis._major_tick_kw["labelcolor"] in ["red", "r"] or ax.xaxis._major_tick_kw[
    "color"
] == (1.0, 0.0, 0.0, 1.0)
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
