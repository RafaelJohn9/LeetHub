class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):  # up to len(s)-3 inclusive
            window = s[i:i+3]
            if len(set(window)) == 3:
                count += 1
        return count
