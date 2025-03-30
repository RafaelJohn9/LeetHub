class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums) # Faster lookups

        count = 0

        for num in nums:
            if num + diff in nums_set and num + diff * 2 in nums_set:
                count += 1
        
        return count