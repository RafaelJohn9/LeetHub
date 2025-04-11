class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_increasing(arr: List[int]) -> bool:
            """Returns True if the given array is strictly increasing."""
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

        n = len(nums)
        count = 0

        # Iterate over all possible subarrays (i, j)
        for i in range(n):
            for j in range(i, n):
                remaining = nums[:i] + nums[j+1:]
                
                if is_increasing(remaining):
                    count += 1

        return count  


