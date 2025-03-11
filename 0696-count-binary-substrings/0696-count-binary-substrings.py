class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_group = 0  # Count of previous group (0s or 1s)
        curr_group = 1  # Count of current group (at least 1 character is there)
        count = 0       # Result count of valid substrings
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_group += 1
            else:
                count += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
        
        count += min(prev_group, curr_group)  # Add the last counted groups
        return count