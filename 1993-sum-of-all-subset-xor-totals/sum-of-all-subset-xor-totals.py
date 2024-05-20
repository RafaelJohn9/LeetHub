class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Initialize the sum of XOR totals
        xor_sum = 0
    
        # Number of elements in the array
        n = len(nums)
    
        # Iterate over all possible subsets (2^n subsets)
        for i in range(1 << n):  # 1 << n is 2^n
            current_xor = 0
        
            # Generate the i-th subset
            for j in range(n):
                # Check if j-th element is in the i-th subset
                if i & (1 << j):
                    current_xor ^= nums[j]
        
            # Add the current XOR total to the sum
            xor_sum += current_xor
    
        return xor_sum
