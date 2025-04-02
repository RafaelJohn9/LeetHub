class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        distinct_avgs = set()

        i = 0
        j = len(nums) - 1

        while i < j:
            distinct_avgs.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        
        return len(distinct_avgs)