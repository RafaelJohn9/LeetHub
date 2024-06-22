class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        count_dict = {0: 1}  

        for num in nums:
            prefix_sum += num % 2
            
            if prefix_sum - k in count_dict:
                count += count_dict[prefix_sum - k]
            
            if prefix_sum in count_dict:
                count_dict[prefix_sum] += 1
            else:
                count_dict[prefix_sum] = 1
        
        return count
