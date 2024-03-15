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
from itertools import zip_longest




def add(df, col):
    for i in df:
        df[col] += i[1]
    return df




def col_to_rgb(col_name):
    rgb = {i: (j // 255, j % 255) for i, j in zip_longest(*[iter(col_name)] * 3)}
    return tuple(rgb[i] for i in range(3))
    
df = pd.DataFrame(data=y)
ax = df.plot(x='X', y='Y')

# make both the x and y axis tick labels red
ax = add(df, 'X')
ax = add(df, 'Y')
ax = col_to_rgb(ax)

# SOLUTION END



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
