import numpy as np
import scipy.stats as ss
def anderson(x1,x2):
	l=len(x1)
	if l==0 or l==1:
		return False
	x1.sort()
	x2.sort()
	p=ss.scoreatpercentile(x1,75)
	q=ss.scoreatpercentile(x2,75)
	return p==q
