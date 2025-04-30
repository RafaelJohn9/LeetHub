class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_in_left: int = nums[0]
        max_so_far: int = nums[0]
        partition_index: int = 0

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < max_in_left:
                partition_index = i
                max_in_left = max_so_far

        return partition_index + 1 