class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_alphanum = lambda x: True if  97 <= ord(x) <= 122 or 48 <= ord(x) <= 57 else False

        left = 0
        right = len(s) - 1

        lower_s = s.lower()

        while left < right:
            if not is_alphanum(lower_s[left]):
                left += 1
                continue
            
            if not is_alphanum(lower_s[right]):
                right -= 1
                continue

            if  lower_s[right] != lower_s[left]:
                return False
            
            left += 1
            right -= 1

        return True
