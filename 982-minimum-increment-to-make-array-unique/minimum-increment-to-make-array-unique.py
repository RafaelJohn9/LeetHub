class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the array to handle elements in order
        nums.sort()
        moves = 0
        
        # Start from the second element and ensure each element is greater than the previous one
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Calculate how many moves we need to make the current number unique
                needed_increment = nums[i - 1] - nums[i] + 1
                nums[i] += needed_increment
                moves += needed_increment
        
        return moves
