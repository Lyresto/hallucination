# import pandas as pd
# import numpy as np
# a = pd.DataFrame(np.array([[1, 2],[3, 4]]), columns=['one', 'two'])
# b = pd.DataFrame(np.array([[5, 6],[7, 8],[9, 10]]), columns=['one', 'two'])



from itertools import zip_longest

def create_dataframe_a_b(*args):
	return pd.concat(map(tuple, zip_longest(*args)), ignore_index=True)
