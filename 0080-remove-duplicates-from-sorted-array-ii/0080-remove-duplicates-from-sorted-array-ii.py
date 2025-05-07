class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        MAX_COUNT = 2
        count = 1
        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= MAX_COUNT:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
                