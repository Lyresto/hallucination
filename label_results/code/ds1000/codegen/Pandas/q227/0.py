import pandas as pd
import numpy as np

a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
b = pd.DataFrame(np.array([[5, 6],[7, 8]]), columns=['one', 'two'])
c = pd.DataFrame(np.array([[9, 10],[11, 12]]), columns=['one', 'two'])
a:
   one  two
0    1    2
1    3    4
b: 
   one  two
0    5    6
1    7    8
c: 
   one  two
0    9    10
1   11   12
END SOLUTION
