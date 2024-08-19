class Solution:
    def minSteps(self, n: int) -> int:
        factor = 2
        steps: int = 0

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        
        return steps