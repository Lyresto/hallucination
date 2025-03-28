import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import pandas as pd
import numpy as np

df = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
###BEGIN SOLUTION
import pandas as pd
df = pd.DataFrame({
'group': ['A', 'A', 'A', 'B', 'B'],
'group_color' : ['green', 'green', 'green', 'blue', 'blue'],
'val1': [5, 2, 3, 4, 5], 
'val2' : [4, 2, 8, 5, 7]
})
  group group_color  val1  val2
0     A       green     5     4
1     A       green     2     2
2     A       green     3     8
3     B        blue     4     5
4     B        blue     5     7


My goal is to get the grouped mean for each of the value columns. In this specific case (with 2 value columns), I can use
df.groupby('group').agg({"group_color": "first", "val1": "mean", "val2": "mean"})
      group_color      val1      val2
group                                
A           green  3.333333  4.666667
B            blue  4.500000  6.000000


but that does not work when the data frame in question has more value columns (val3, val4 etc.).
Is there a way to dynamically take the mean of "all the other columns" or "all columns containing val in their names"?


A:
<code>
import pandas as pd


df = pd.DataFrame({ 'group': ['A', 'A', 'A', 'B', 'B'], 'group_color' : ['green', 'green', 'green', 'blue', 'blue'], 'val1': [5, 2, 3, 4, 5], 'val2' : [4, 2, 8, 5, 7],'val3':[1,1,4,5,1] })

###END SOLUTION

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)