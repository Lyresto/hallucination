def state(df, k):
	s = 0
	for i in range(len(df[k])):
		if k =='state':
			s = s + df[k][i]
		elif k == 'col2' and df[k][i] > 50:
			s = s + 50
		elif k == 'col3' and df[k][i] > 50:
			s = s + 100
		else:
			s = s + df[k][i]
	return s
