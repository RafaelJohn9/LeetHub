class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        insert_pos = 0

        for i in range(n):
            if nums[i] != val:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos