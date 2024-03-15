from fractions import Fraction

result = Fraction(numerator, denominator).limit_denominator()
result = (result.numerator, result.denominator)
