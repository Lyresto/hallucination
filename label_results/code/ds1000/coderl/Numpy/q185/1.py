# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:25:18 2020

@author: Srikar
"""
import numpy as np

def generate_column(df, column_name):
	result = np.zeros(len(df))
	for i, val in enumerate(df[column_name]):
		result[i] = val
	return pd.DataFrame(result)
