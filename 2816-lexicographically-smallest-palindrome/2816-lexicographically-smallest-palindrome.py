class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            if s_list[i] != s[j]:
                smaller_char = min(s_list[i], s_list[j])
                s_list[i] = s_list[j] = smaller_char

            i += 1
            j -= 1
        
        return ''.join(s_list)