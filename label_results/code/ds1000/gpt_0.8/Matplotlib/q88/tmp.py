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
fig, ax = plt.subplots(1, 1)
plt.xlim(1, 10)
plt.xticks(range(1, 10))
ax.plot(y, x)

# change the second x axis tick label to "second" but keep other labels in numerical
# SOLUTION START
# Get the current x-axis tick labels
labels = [item.get_text() for item in ax.get_xticklabels()]

# Change the second tick label to "second"
labels[1] = "second"

# Set the new tick labels
ax.set_xticklabels(labels)



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
assert ax.xaxis.get_ticklabels()[1]._text == "second"
assert ax.xaxis.get_ticklabels()[0]._text == "1"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
