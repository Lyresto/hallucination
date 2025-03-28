import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import pandas as pd
import matplotlib.pyplot as plt

values = [[1, 2], [3, 4]]
df = pd.DataFrame(values, columns=["Type A", "Type B"], index=["Index 1", "Index 2"])

# Plot values in df with line chart
# label the x axis and y axis in this plot as "X" and "Y"
# SOLUTION START
plt.plot(df["Type A"], df["Type B"])
plt.xlabel("Type A")
plt.ylabel("Type B")
plt.title("Plot title")
plt.show()
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
ax = plt.gca()
assert len(ax.get_lines()) == 2
assert ax.xaxis.label._text == "X"
assert ax.yaxis.label._text == "Y"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
