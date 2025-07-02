class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_window = 0
        min_len = float('inf')

        for right in range(len(nums)):
            sum_window += nums[right]

            # Shrink window while condition is met
            while sum_window >= target:
                min_len = min(min_len, right - left + 1)
                sum_window -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
