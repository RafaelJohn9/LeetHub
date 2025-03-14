class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s: str = ""

        for letter in s:
            if letter == "#":
                result_s = result_s[:-1]
            else:
                result_s += letter
        
        result_t: str = ""

        for letter in t:
            if letter == "#":
                result_t = result_t[:-1]
            else:
                result_t += letter

        return result_s == result_t
        