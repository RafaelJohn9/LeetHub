class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        
        xor_all = 0

        for num in nums:
            xor_all ^= num
        
        rightmost_set_bit = xor_all & -xor_all

        num1, num2 = 0, 0

        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]