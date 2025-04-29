class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_pos = 0
        n = len(nums)

        if n == 1:
            return n

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                continue
            
            nums[insert_pos] = nums[i]
            insert_pos += 1
        
        nums[-1], nums[insert_pos] = nums[insert_pos], nums[-1]
        insert_pos += 1

        return insert_pos