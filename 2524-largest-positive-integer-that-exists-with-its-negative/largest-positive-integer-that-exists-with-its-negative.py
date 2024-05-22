class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        find the max num check if its negative exists
        if it exists return it
        else continue iterating
        """

        while len(nums):
            largest_num = max(nums)
            try:
                smallest_num_index =  nums.index(largest_num * -1)
                return largest_num
            except ValueError:
                del(nums[nums.index(largest_num)])
                continue
        return -1