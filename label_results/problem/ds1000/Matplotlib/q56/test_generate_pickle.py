import pickle
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()


import matplotlib.pyplot as plt
import numpy as np, pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

# Make a seaborn joint regression plot (kind='reg') of 'total_bill' and 'tip' in the tips dataframe
# do not use scatterplot for the joint plot
# SOLUTION START
sns.jointplot(
    x="total_bill", y="tip", data=tips, kind="reg", joint_kws={"scatter": False}
)
# SOLUTION END

os.makedirs('ans', exist_ok=True)
os.makedirs('input', exist_ok=True)
plt.savefig('ans/oracle_plot.png', bbox_inches ='tight')
with open('input/input1.pkl', 'wb') as file:
    # input is already contained in code_context.txt so we dump a dummy input object
    pickle.dump(None, file)
with open('ans/ans1.pkl', 'wb') as file:
    # test does not require a reference solution object so we dump a dummpy ans object
    pickle.dump(None, file) 
