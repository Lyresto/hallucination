import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

x = np.arange(10)
y = np.linspace(0, 1, 10)

# Plot y over x with a scatter plot
# Use the "Spectral" colormap and color each data point based on the y-value
# SOLUTION START
# IMPORTANT: y should be a column of x.
# Use the `matplotlib.colors` library to color the points.
# You can use any number of colors for x.

y_values = pd.Series(y).plot(x, color='#AAAAAA')

# Plot a line of x values with a legend.
# Use the `matplotlib.lines` library to draw lines.
x_lines = pd.DataFrame({'x': x})
y_lines = pd.DataFrame({'y': y})
x_lines.plot(x, y, linestyle='-', label='y')
y_lines.plot(x, y, linestyle='', label='x')

# Use `set_ylim` to set the y-axis limits.
y_lines['y'] = y_lines['y'].shift(1)
y_lines.set_ylim(0, 10)

# Use `set_xticks` to set the x-axis ticks.
x_lines['x'] = x_lines['x'].shift(1)
x_lines.set_xticks([0, 1])

# Add a legend with one line at a time.
ax = x_lines.plot(x_lines['x'], y_lines['y'], linewidth=2)

# Remove the axis line by default.
ax.set_xlabel('x')
ax.set_ylabel('y')

# Remove the legend by default.
ax.legend(loc='best')

# Show the plot.




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
assert len(ax.collections) == 1
ax.collections[0].get_cmap().name == "Spectral"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
