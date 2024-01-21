class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        stairs = [0] * n
        indexOf = lambda x: x - 1
        stairs[indexOf(1)] = 1
        stairs[indexOf(2)] = 2

        for stair in range(3, n + 1):
            stairs[indexOf(stair)] = stairs[indexOf(stair - 1)] + stairs[indexOf(stair - 2)]
        
        return stairs[indexOf(n)]