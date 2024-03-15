# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:45:48 2020

@author: kurts
"""
import numpy as np
df = pd.DataFrame.from_dict({'UserId': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
	'ProductId': [1, 4, 7, 4, 2, 1, 1, 4, 7, 4, 2, 1, 1, 4, 7],
	'Quantity': [6, 1, 3, 2, 7, 2, 6, 1, 3, 2, 7, 2, 6, 1, 3]})
ans = np.zeros_like(df['Quantity'])
for i in range(0, len(df['UserId'])):
	num = int(0.8*len(df['UserId']))
	df['UserId'] = df['UserId'][num:]+df['UserId'][:num]
	ans[i] = df['Quantity'][i]

print(ans)
