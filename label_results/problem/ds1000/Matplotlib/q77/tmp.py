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
z = np.arange(10)
a = np.arange(10)

# plot y over x and z over a in two different subplots
# Set "Y and Z" as a main title above the two subplots
# SOLUTION START
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.plot(x, y)
ax1.set_title('Y')

ax2.plot(z, a)
ax2.set_title('Z')

fig.suptitle('Y and Z')




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
assert f._suptitle.get_text() == "Y and Z"
for ax in f.axes:
    assert ax.get_title() == ""
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
