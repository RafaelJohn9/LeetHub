import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
            
        for a in range(int(math.sqrt(c)) + 1):
            a_squared = a * a
            b_squared = c - a_squared
            b = int(math.sqrt(b_squared))
            if b * b == b_squared:
                return True
        return False
