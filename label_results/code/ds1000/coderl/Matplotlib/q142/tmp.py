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

# Plot y over x in a line chart. Show x axis tick labels but hide the x axis ticks
# SOLUTION START
from itertools import chain




def pchart(df, x=None, y=None):
    if x is None:
        x = np.arange(10)
    if y is None:
        y = np.arange(10)
    
    return (
        chain(
            df.plot(x=x, y=y).set_xlabels([]).show(xaxis_label=False),
            df.plot(x=x, y=y).set_xlabels([x.min(), x.max()]).show(xaxis_label=True),
        )
    )



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
assert not ax.xaxis._major_tick_kw["tick1On"]
assert ax.xaxis._major_tick_kw["label1On"]
assert len(ax.get_xticks()) > 0
for l in ax.get_xticklabels():
    assert l.get_text() != ""
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
