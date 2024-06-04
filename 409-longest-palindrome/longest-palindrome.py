class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for letter in s:
            if count.get(letter, None):
                count[letter] += 1
            else:
                count[letter] = 1
        
        length_of_palindrome = 0
        for value in count.values():
            if value % 2 == 0:
                length_of_palindrome += value
            else:
                length_of_palindrome += value - 1
        return length_of_palindrome if len(s) == length_of_palindrome else length_of_palindrome + 1