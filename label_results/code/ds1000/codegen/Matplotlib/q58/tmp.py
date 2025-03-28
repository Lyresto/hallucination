import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(
    {
        "celltype": ["foo", "bar", "qux", "woz"],
        "s1": [5, 9, 1, 7],
        "s2": [12, 90, 13, 87],
    }
)

# For data in df, make a bar plot of s1 and s1 and use celltype as the xlabel
# Make the x-axis tick labels rotate 45 degrees
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
ax = plt.gca()
plt.show()
assert len(ax.patches) > 0
assert len(ax.xaxis.get_ticklabels()) > 0
for t in ax.xaxis.get_ticklabels():
    assert t._rotation == 45
all_ticklabels = [t.get_text() for t in ax.xaxis.get_ticklabels()]
for cell in ["foo", "bar", "qux", "woz"]:
    assert cell in all_ticklabels
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
