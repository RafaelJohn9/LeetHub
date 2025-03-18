class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        tortoise, hare = 0, 1
        n = len(nums)

        while tortoise < n and hare < n:
            if nums[tortoise] % 2 == 0:
                tortoise += 2  # Move to next even index
            elif nums[hare] % 2 == 1:
                hare += 2  # Move to next odd index
            else:
                nums[tortoise], nums[hare] = nums[hare], nums[tortoise]
                tortoise += 2
                hare += 2
        
        return nums