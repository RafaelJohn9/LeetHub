class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, -1
        max_seen = float('-inf')
        min_seen = float('inf')
        
        # Traverse left to right
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]
        
        # Traverse right to left
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]
        
        return right - left + 1 if right != -1 else 0
