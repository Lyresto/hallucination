import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt
import numpy as np, pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

# Make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# change the line color in the regression to green but keep the histograms in blue
# SOLUTION START



def reg_plot(tips):
    df = tips.copy()
    df['tip'], df['total_bill'] = df['tip'], df['total_bill']
    sns.jointplot('total_bill', 'tip', data=df, kind='reg')
    return plt.gcf()



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
assert len(f.axes[0].get_lines()) == 1
assert f.axes[0].get_xlabel() == "total_bill"
assert f.axes[0].get_ylabel() == "tip"

assert f.axes[0].get_lines()[0]._color in ["green", "g", "#008000"]
for p in f.axes[1].patches:
    assert p.get_facecolor()[0] != 0
    assert p.get_facecolor()[2] != 0
for p in f.axes[2].patches:
    assert p.get_facecolor()[0] != 0
    assert p.get_facecolor()[2] != 0
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
