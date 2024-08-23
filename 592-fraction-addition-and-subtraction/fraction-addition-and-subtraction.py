from fractions import Fraction
import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # initialize the result
        result = Fraction(0, 1)

        for fraction in fractions:
            result += Fraction(fraction)

        return f"{result.numerator}/{result.denominator}"