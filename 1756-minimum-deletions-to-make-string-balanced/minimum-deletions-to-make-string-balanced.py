class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Calculate the minimum number of deletions required to make the string balanced.
        A string is balanced if there is no pair of indices (i, j) such that i < j,
        s[i] = 'b', and s[j] = 'a'.
        
        Args:
        s (str): The input string containing only 'a' and 'b'.
        
        Returns:
        int: The minimum number of deletions required to balance the string.
        """
        # Count the number of 'b's seen so far
        b_count = 0
        # Count the minimum deletions required
        deletions = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:  # char == 'a'
                # We need to delete this 'a' or the previous 'b's
                # We choose the minimum deletions required
                deletions = min(deletions + 1, b_count)
        
        return deletions
