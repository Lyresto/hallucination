import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt
import numpy as np

box_position, box_height, box_errors = np.arange(4), np.ones(4), np.arange(1, 5)
c = ["r", "r", "b", "b"]
fig, ax = plt.subplots()
ax.bar(box_position, box_height, color="yellow")

# Plot error bars with errors specified in box_errors. Use colors in c to color the error bars
# SOLUTION START



def bar(pos, height, err, c):
    for i, e in enumerate(err):
        ax.errorbar(pos + i, height + e, c=c[i])
    
# SOLUTION END



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
assert len(ax.get_lines()) == 4
line_colors = []
for line in ax.get_lines():
    line_colors.append(line._color)
assert set(line_colors) == set(c)
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
