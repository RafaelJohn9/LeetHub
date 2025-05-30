class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)
        i = 0
        j = 1
        result = set()

        while j < n:
            if i == j:
                j += 1
                continue

            if abs(nums[i] - nums[j]) == k:
                subset = (nums[i], nums[j])
                result.add(subset)
                j += 1
            elif abs(nums[i] - nums[j]) > k:
                i += 1
            else:
                j += 1
        
        return len(result)