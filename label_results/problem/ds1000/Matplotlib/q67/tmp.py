import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = [2.56422, 3.77284, 3.52623]
b = [0.15, 0.3, 0.45]
c = [58, 651, 393]

# make scatter plot of a over b and annotate each data point with correspond numbers in c
# SOLUTION START
plt.scatter(b, a)
for i, txt in enumerate(c):
    plt.annotate(txt, (b[i], a[i]))
plt.xlabel('b')
plt.ylabel('a')




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
assert len(ax.texts) == 3
for t in ax.texts:
    assert int(t.get_text()) in c
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
