import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")[["bill_length_mm", "species", "sex"]]

# Make a stripplot for the data in df. Use "sex" as x, "bill_length_mm" as y, and "species" for the color
# Remove the legend from the stripplot
# SOLUTION START

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
f = plt.gcf()
assert len(f.axes) == 1
ax = plt.gca()
assert len(ax.collections) > 0
assert ax.legend_ is None or not ax.legend_._visible
assert ax.get_xlabel() == "sex"
assert ax.get_ylabel() == "bill_length_mm"
all_colors = set()
for c in ax.collections:
    all_colors.add(tuple(c.get_facecolors()[0]))
assert len(all_colors) == 3
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
