import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import seaborn as sns
import matplotlib.pylab as plt
import pandas
import numpy as np

df = pandas.DataFrame(
    {
        "a": np.arange(1, 31),
        "b": ["A",] * 10 + ["B",] * 10 + ["C",] * 10,
        "c": np.random.rand(30),
    }
)

# Use seaborn FaceGrid for rows in "b" and plot seaborn pointplots of "c" over "a"
# In each subplot, show xticks of intervals of 1 but show xtick labels with intervals of 2
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
assert len(f.axes) == 3
xticks = f.axes[-1].get_xticks()
diff = xticks[1:] - xticks[:-1]
assert np.all(diff == 1)
xticklabels = []
for label in f.axes[-1].get_xticklabels():
    if label.get_text() != "":
        xticklabels.append(int(label.get_text()))
xticklabels = np.array(xticklabels)
diff = xticklabels[1:] - xticklabels[:-1]
assert np.all(diff == 2)
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
