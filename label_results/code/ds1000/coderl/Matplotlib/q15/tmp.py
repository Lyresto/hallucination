import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.randn(10)
y = np.random.randn(10)

# in plt.plot(x, y), use a plus marker and give it a thickness of 7
# SOLUTION START
from itertools import zip_longest

df = pd.DataFrame(zip_longest(x, y), columns=['x', 'y'])
for p, (ax1, ax2) in enumerate(df.plot.values()):
    ax2.set_linewidth(7)
    ax1.set_markersize(2)
    p += 1



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
assert len(ax.lines) == 1
assert ax.lines[0].get_markeredgewidth() == 7
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
