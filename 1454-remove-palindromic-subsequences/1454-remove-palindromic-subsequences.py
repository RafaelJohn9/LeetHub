class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s: str):
            return s == s[::-1]
        
        return 1 if is_palindrome(s) else 2