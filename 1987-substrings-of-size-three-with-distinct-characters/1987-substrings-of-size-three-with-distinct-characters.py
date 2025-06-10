class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        first_str = s[:3]

        count = 0
        for letter in s[3:]:
            subset = set(first_str)

            if len(subset) == 3:
                count += 1
            
            first_str = first_str[1:] + letter
        
        return count if len(set(first_str)) != 3 else count + 1