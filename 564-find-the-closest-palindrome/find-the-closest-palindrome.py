class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # Edge case for numbers like "1000"
        candidates.add(str(10 ** (length - 1) - 1))
        # Edge case for numbers like "999"
        candidates.add(str(10 ** length + 1))
        
        # Middle part to consider
        prefix = int(n[:(length + 1) // 2])
        
        for i in [-1, 0, 1]:
            candidate = str(prefix + i)
            if length % 2 == 0:
                candidate += candidate[::-1]
            else:
                candidate += candidate[-2::-1]
            candidates.add(candidate)
        
        candidates.discard(n)  # remove the original number itself
        
        # Find the closest by absolute difference, with ties going to the smaller number
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))