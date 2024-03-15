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

# Plot y over x in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
df = pd.DataFrame({'x': x, 'y': y})

ax = df.plot.line(x='x', y='y')
ax.set_title('Line Plot', fontsize=16)


# Plot y over x in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# df = pd.DataFrame({'x': x, 'y': y})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Plot', fontsize=16)

# Plot y over x in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min, x_max, y_min, y_max = df['x'].min(), df['x'].max(), df['y'].min(), df['y'].max()
# df = df.rename(columns={'x': 'x_min', 'y': 'x_max', 'x_min': 'y_min', 'y_min': 'y_max'})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Chart', fontsize=16)

# Plot x over y in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min, x_max, y_min, y_max = df['x'].min(), df['x'].max(), df['y'].min(), df['y'].max()
# df = df.rename(columns={'x': 'x_min', 'y': 'x_max', 'x_min': 'y_min', 'y_min': 'y_max'})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Chart', fontsize=16)

# Plot x over y in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min,


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
assert len(ax.get_lines()) > 0
no_tick_label = np.all([l._text == "" for l in ax.get_xaxis().get_majorticklabels()])
tick_not_visible = not ax.get_xaxis()._visible
ax.get_xaxis()

assert no_tick_label or tick_not_visible
assert ax.get_xaxis().get_label().get_text() == "x"
assert ax.get_yaxis().get_label().get_text() == "y"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
