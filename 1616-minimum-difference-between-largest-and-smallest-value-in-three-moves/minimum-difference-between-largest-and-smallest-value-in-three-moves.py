from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        # Considering the four cases
        return min(nums[-1] - nums[3],   # Change 3 smallest
                   nums[-2] - nums[2],   # Change 2 smallest, 1 largest
                   nums[-3] - nums[1],   # Change 1 smallest, 2 largest
                   nums[-4] - nums[0])   # Change 3 largest
