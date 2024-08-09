class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif 0 < n < 2:
            return 1
        
        first = 1
        second = 1

        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second