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
# Make the line of the x axis red
# SOLUTION START
plt.plot(x, y)
plt.xlabel("X")
plt.axhline(y=0, color='r')



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
assert ax.spines["bottom"].get_edgecolor() == "red" or ax.spines[
    "bottom"
].get_edgecolor() == (1.0, 0.0, 0.0, 1.0)
assert ax.spines["top"].get_edgecolor() != "red" and ax.spines[
    "top"
].get_edgecolor() != (1.0, 0.0, 0.0, 1.0)
assert ax.spines["left"].get_edgecolor() != "red" and ax.spines[
    "left"
].get_edgecolor() != (1.0, 0.0, 0.0, 1.0)
assert ax.spines["right"].get_edgecolor() != "red" and ax.spines[
    "right"
].get_edgecolor() != (1.0, 0.0, 0.0, 1.0)
assert ax.xaxis.label._color != "red" and ax.xaxis.label._color != (1.0, 0.0, 0.0, 1.0)
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
