import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt

labels = ["a", "b"]
height = [3, 4]

# Use polar projection for the figure and make a bar plot with labels in `labels` and bar height in `height`
# SOLUTION START
from itertools import zip_longest

fig, ax = plt.subplots()
ax.bar(zip_longest(range(len(labels)), height, labels=labels, color='r'))
ax.grid(True)

# Plot different bar positions
# ax.plot(zip_longest(range(len(labels)), height, label='a')
# ax.plot(zip_longest(range(len(labels)), height, label='b')
#... by using polar projection, each bar will have different x-coordinates.

# plot another bar with different x-coordinates, coloring each bar according to height
ax.bar(zip_longest(range(len(labels)), (height[0] + 1), color='g'), zip_longest(range(len(labels)), height, color='b'), label='a')
ax.bar(zip_longest(range(len(labels)), (height[1] + 1), color='r'), zip_longest(range(len(labels)), height, color='g'), label='b')

# Remove y-axis labels
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Add x-axis title and tick labels
ax.set_xlabel('Bar Height')
ax.set_ylabel('Label')

# Show plot




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
assert ax.name == "polar"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
