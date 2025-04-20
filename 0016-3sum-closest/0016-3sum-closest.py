class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        result = float("inf")

        for i in range(n):
                if i > 0 and nums[i] == nums[i -1]:
                    continue

                j = i + 1
                k = n - 1

                while j < k:
                    total = nums[i] + nums[j] + nums[k]

                    total_difference = abs(total - target)
                    result_difference = abs(result - target)

                    if total_difference < result_difference:
                        result = total
                    
                    if total == target:
                        return total
                    elif total < target:
                        j += 1
                    else:
                        k -= 1
        
        return result