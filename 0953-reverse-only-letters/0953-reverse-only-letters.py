class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s_list = list(s)

        while left < right:
            while left < right and not s_list[left].isalpha():
                left += 1
            while left < right and not s_list[right].isalpha():
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)