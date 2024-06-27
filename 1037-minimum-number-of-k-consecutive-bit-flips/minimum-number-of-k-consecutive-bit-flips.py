class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = [0] * (n + 1)  # Difference array to track flips
        flip_count = 0  # Number of flips affecting the current position
        result = 0  # Total number of flips performed

        for i in range(n):
            flip_count ^= flipped[i]  # Update the current flip effect
            if nums[i] == flip_count:  # If nums[i] is 0 after current flips, we need to flip it
                if i + k > n:  # If flipping here exceeds array bounds, return -1
                    return -1
                result += 1  # Increment the number of flips performed
                flip_count ^= 1  # Mark the current position as flipped
                flipped[i + k] ^= 1  # Schedule to remove flip effect after k positions

        return result