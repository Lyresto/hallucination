import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt

# Make a solid vertical line at x=3 and label it "cutoff". Show legend of this plot.
# SOLUTION START
plt.axvline(x=3, color='r', linestyle='--', label='cutoff')
plt.legend()



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
assert len(ax.get_lines()) == 1
assert ax.get_lines()[0]._x[0] == 3
assert len(ax.legend_.get_lines()) == 1
assert ax.legend_.get_texts()[0].get_text() == "cutoff"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
