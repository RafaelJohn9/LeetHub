class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n, k):
            if n == 1:
                return 0
            else:
                return (josephus(n - 1, k) + k) % n
        
        # Add 1 to convert from 0-based index to 1-based index
        return josephus(n, k) + 1