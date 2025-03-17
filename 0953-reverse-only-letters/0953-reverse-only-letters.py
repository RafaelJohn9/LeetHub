class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0 
        right = len(s) - 1

        s_list = list(s)

        while left < right:
            if ord(s_list[left].lower()) < ord('a') or ord(s_list[left].lower()) > ord('z'):
                left += 1
                continue
            
            if ord(s_list[right].lower()) < ord('a') or ord(s_list[right].lower()) > ord('z'):
                right -= 1
                continue
            
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return ''.join(s_list)