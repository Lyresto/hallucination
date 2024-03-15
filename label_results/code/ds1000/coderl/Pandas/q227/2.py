import itertools

def create_dataframe_lists(df):
	for i, rows in enumerate(df.itertuples()):
		yield tuple(rows)

def cycle_dataframe_lists(df):
	# I have to find all possible combinations of elements in the tuple
	# (all combinations of 1 or 2 are the same)
	# then we need to find the first one and set it as the first element 
	# and then cycle through it.
	# We need to find the indices of the 2 different elements 
	# and then use them to generate the new tuple, 
#  and finally return it
	#
	# I think the loop is as follows:
	# - if there are two different elements in a tuple, there are 2 cases
	#   in which case we have to iterate through the columns and use
	#   the first one to generate the tuple
	# - if there are no different elements in a tuple, there are 2 cases
	#   in which case we have to iterate through columns and use
	#   the first one to generate the tuple
	# - if there are no different elements in a tuple, there are 2 cases
	#   in which case we have to iterate through columns and use the
	#   first one to generate the tuple
	#
	# This is because each tuple can be made of 4 columns and
	# each column is composed of 3 different elements
	#
	# The loop is then:
	# - for each column, we have to iterate through it and set each 
	#   element to the index of the tuple
	# - for each row, we have to iterate through it and set each element 
	#   to the index of the tuple
	#
	# This is because for each column, we have to iterate through it and 
	# set each element to the index of the tuple
	#
	# This is because if there are 4 different elements in a tuple, 
	# the loop is as follows:
	# - for each column, there are 2 cases in which case we have to iterate
	#   through the columns and use the first one to generate the tuple
	# - for each column, there are 2 cases in which case we have to iterate
	#   through the columns and use the first one to generate