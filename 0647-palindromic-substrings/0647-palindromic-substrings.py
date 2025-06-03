class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        for i in range(n):
            j = i + 1

            while j < n:
                if is_palindrome(s[i:j+1]):
                    count += 1
                
                j += 1
        
        return count
