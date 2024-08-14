class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
    
        # Calculate points
        for num in nums:
            points[num] += num
    
        # Initialize the dp array
        dp = [0] * (max_num + 1)
    
        dp[0] = 0
        dp[1] = points[1]
    
        # Fill dp array using the recurrence relation
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
    
        return dp[max_num] 