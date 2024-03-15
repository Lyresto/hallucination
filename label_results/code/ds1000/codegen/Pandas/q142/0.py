import pandas as pd


df = pd.DataFrame({'col1': {0: 'a', 1: 'b', 2: 'c'},
                   'col2': {0: 1, 1: 3, 2: 5},
                   'col3': {0: 2, 1: 4, 2: 6},
                   'col4': {0: 3, 1: 6, 2: 2},
                   'col5': {0: 7, 1: 2, 2: 3},
                   'col6': {0: 2, 1: 9, 2: 5},
                  })
df.columns = [list('AAAAAA'), list('BBCCDD'), list('EFGHIJ')]
