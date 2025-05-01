class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        high = n - 1
        low = 0
        

        while low < high:
            if not s[low].isalnum():
                low += 1
                continue
            
            if not s[high].isalnum():
                high -= 1
                continue

            if not s[low] == s[high]:
                return False
            
            
            low += 1
            high -= 1
        

        return True