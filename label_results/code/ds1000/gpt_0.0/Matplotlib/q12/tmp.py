import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn

seaborn.set(style="ticks")

numpy.random.seed(0)
N = 37
_genders = ["Female", "Male", "Non-binary", "No Response"]
df = pandas.DataFrame(
    {
        "Height (cm)": numpy.random.uniform(low=130, high=200, size=N),
        "Weight (kg)": numpy.random.uniform(low=30, high=100, size=N),
        "Gender": numpy.random.choice(_genders, size=N),
    }
)

# make seaborn relation plot and color by the gender field of the dataframe df
# SOLUTION START
seaborn.relplot(x="Height (cm)", y="Weight (kg)", hue="Gender", data=df)



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
all_colors = set()
for c in ax.collections:
    colors = c.get_facecolor()
    for i in range(colors.shape[0]):
        all_colors.add(tuple(colors[i]))
assert len(all_colors) == 4
assert ax.get_xlabel() == "Weight (kg)"
assert ax.get_ylabel() == "Height (cm)"
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
