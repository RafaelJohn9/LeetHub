class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captures = 0
        n = len(forts)
        
        i = 0
        while i < n:
            if forts[i] == 1 or forts[i] == -1:
                j = i + 1
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[i] + forts[j] == 0:  # enemy fort on the other end
                    max_captures = max(max_captures, j - i - 1)
                i = j
            else:
                i += 1
        
        return max_captures
