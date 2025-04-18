class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        result = set()

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return [list(subset) for subset in result]