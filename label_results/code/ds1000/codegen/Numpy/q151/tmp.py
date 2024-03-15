import pickle


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
A, B = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2,3,3,3,4,5,6,7,8,8])
B = np.array([1,2,8])
C =... # put solution in this variable
BEGIN SOLUTION
<code>
import numpy as np
A = np.array([1,1,2
#print(C)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(C, file)
