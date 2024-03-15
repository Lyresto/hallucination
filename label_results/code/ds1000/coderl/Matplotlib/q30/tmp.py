import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y = 2 * np.random.rand(10)
x = np.arange(10)

# make the y axis go upside down
# SOLUTION START
from itertools import zip_longest




def downsample(arr, n):
    n = int(n)
    arr = list(arr)
    s = n // 2
    a = arr[:s] + arr[-s:]
    b = arr[:s]
    return a, b
    




def plot(x, y):
    ax = plt.gca()
    ax.bar(x, y, width=1)
    return ax.get_yaxis().get_majorticklines()[0]




def weighted_mean(df):
    w = 1.0 * len(df)
    df.cumsum().cumsum().plot(kind='bar', ax=plt.gca())
    return df.cumsum().cumsum() / w

df = pd.DataFrame({'x': x, 'y': y})
df = downsample(df['x'], n=10)
df = downsample(df['y'], n=10)
# df = weighted_mean(df)

ans = plot(df['x'], df['y'])
print(ans)



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
assert ax.get_ylim()[0] > ax.get_ylim()[1]
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
