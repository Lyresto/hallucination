import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")[
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
]

# make a seaborn scatter plot of bill_length_mm and bill_depth_mm
# use markersize 30 for all data points in the scatter plot
# SOLUTION START
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", s=30)



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
assert len(ax.collections[0].get_sizes()) == 1
assert ax.collections[0].get_sizes()[0] == 30
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
