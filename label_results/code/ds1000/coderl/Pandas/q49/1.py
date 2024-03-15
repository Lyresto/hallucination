import pandas as pd

def aggregate_rows_not_in_c(df, section_left, section_right):
	left = []
	for i in range(section_left, section_right+1):
		left.append(df.loc[i-1:i])
	return sum(sum(left[j] / len(left[j])) for j in range(len(df.index) - section_left + 1)) / (section_right - section_left + 1)
