import numpy as np
c = np.array([[[ 75, 763]],
              [[ 57, 763]],
              [[ np.nan, 749]],
              [[ 75, 749]]])
CNTS = [np.array([[[  np.nan, 1202]],
                  [[  63, 1202]],
                  [[  63, 1187]],
                  [[  78, 1187]]]),
        np.array([[[ 75, 763]],
                  [[ 57, 763]],
                  [[ np.nan, 749]],
                  [[ 75, 749]]]),
        np.array([[[ 72, 742]],
                  [[ 58, 742]],
                  [[ 57, 741]],
                  [[ 57, np.nan]],
                  [[ 58, 726]],
                  [[ 72, 726]]]),
        np.array([[[ np.nan, 194]],
                  [[ 51, 194]],
                  [[ 51, 179]],
                  [[ 66, 179]]])]

result = any(np.array_equal(c, cnt) for cnt in CNTS)
print(result)
