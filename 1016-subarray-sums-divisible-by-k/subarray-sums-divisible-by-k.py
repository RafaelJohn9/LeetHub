class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
        
            # Adjust for negative remainders
            if remainder < 0:
                remainder += k

            if remainder in prefix_counts:
                count += prefix_counts[remainder]
        
            if remainder in prefix_counts:
                prefix_counts[remainder] += 1
            else:
                prefix_counts[remainder] = 1
    
        return count
