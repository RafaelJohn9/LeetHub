class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            j = i
            for k in range(len(needle)):
                if j < len(haystack) and haystack[j] == needle[k]:
                    j += 1
                else:
                    break
                
                if k == len(needle) - 1:
                    return i

        return -1