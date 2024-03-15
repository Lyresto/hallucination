from math import gcd

def reduce_fractions(numerator, denominator):
	num = numerator
	den = denominator
	f = f = gcd(num, den)
	while f:
		num, den = num / f, den / f
		f = gcd(num, den)
	return (float(num), float(den)) if num!= 0 and den!= 0 else (float("nan"), float("nan"))
