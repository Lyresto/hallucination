from fractions import Fraction

if denominator == 0:
    result = (float('nan'), float('nan'))
else:
    result = Fraction(numerator, denominator).as_integer_ratio()

result = tuple(result)
