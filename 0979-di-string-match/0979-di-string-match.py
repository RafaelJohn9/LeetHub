class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low = 0
        high = n

        response = []
        i = 0
        while i < n:
            if s[i] == "I":
                response.append(low)
                i += 1
                low += 1
            else:
                response.append(high)
                i += 1
                high -= 1
        
        response.append(low)

        return response