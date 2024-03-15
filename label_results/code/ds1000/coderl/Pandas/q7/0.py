# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:46:52 2019

@author: Greg
"""
import collections

def drop_duplicates(df, keep_first=False):
	# Your code goes here
	output = []
	for key in df.keys():
		value = df[key]
		if keep_first and value.duplicated():
			continue
		output.append([key, value.value, value.duplicated()])

	return output
