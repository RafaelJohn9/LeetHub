class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Edge case: k should not be zero
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums) - 1))
        
        # Dictionary to store the remainder and corresponding index
        remainder_dict = {0: -1}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k
            
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                remainder_dict[remainder] = i

        return False