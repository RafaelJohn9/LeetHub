class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        i = 0
        zero_count = 0

        while i < n - 1:
            if nums[i] == 0:
                zero_count += 1
                i += 1
            elif nums[i] == nums[i + 1]:
                result.append(nums[i] * 2)
                zero_count += 1
                i += 2
            else:
                result.append(nums[i])
                i += 1

        if i < n:
            result.append(nums[-1])
        
        result.extend([0] * zero_count)
        return result