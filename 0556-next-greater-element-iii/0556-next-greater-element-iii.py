class Solution:
    def nextGreaterElement(self, n: int) -> int:
        INT_MAX_VALUE = 2_147_483_647
         
        nums = list(str(n))
        length = len(nums)
        i = length - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        

        j = length - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1:] = reversed(nums[i + 1:])
        new_num = int("".join(nums))

        return new_num if new_num <= INT_MAX_VALUE else -1