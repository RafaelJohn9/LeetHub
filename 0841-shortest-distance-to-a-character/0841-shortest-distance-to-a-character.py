class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('inf')] * n

        shortest_c = -float("inf")

        # left iteration
        for i in range(n):
            if s[i] == c:
                shortest_c = i

            result[i] = abs(i - shortest_c)
        
        shortest_c = float("inf")
        for j in range(n - 1, -1, -1):
            if s[j] == c:
                shortest_c = j
            
            result[j] = min(result[j], abs(j - shortest_c))
        
        return result

