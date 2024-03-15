import pickle
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0, 2 * np.pi, 10)
y = np.cos(x)
plt.plot(x, y, label="sin")

# rotate the x axis labels clockwise by 45 degrees
# SOLUTION START
import numpy as np




def sin(x):
    x = np.radians(x)
    return np.sin(x)




def cos(x):
    x = np.radians(x)
    return np.cos(x)

df = pd.DataFrame({'x': [0, 0, 2 * np.pi, 2 * np.pi * 2], 'y': [1, 1, sin(1), sin(2)]})
df.plot(kind='line', x='x', y='y', label='sin')
df.plot(kind='scatter', x='x', y='y', color='y', marker='o')
df.plot(kind='line', x='x', y='sin(x)', label='sin')
df.plot(kind='scatter', x='x', y='cos(x)', label='cos')
df.plot(kind='line', x='x', y='sin(2x)', label='sin')

df.x = df.x.rolling(2).mean()
df.y = df.y.rolling(2).mean()

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='sin(2x)', label='sin')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='sin(2x)', label='sin')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='cos(2x)', label='cos')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.grid(True, which='minor')

df.y.grid(True, which='minor')

df.y


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
x = ax.get_xaxis()
labels = ax.get_xticklabels()
for l in labels:
    assert l.get_rotation() == 45
with open('result/result_1.pkl', 'wb') as file:
    # or if execution-based test passed, we save True to the result file
    pickle.dump(True, file)     
