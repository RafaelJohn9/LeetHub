class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
            
        return insert_pos