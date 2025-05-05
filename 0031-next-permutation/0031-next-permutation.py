class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n <= 1:
            return

        # Do a pass to check to get the number needing switching
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        

        # Find the appropriate element to switch with
        j = n - 1
        if i >= 0:
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the suffix elements from decending order
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1