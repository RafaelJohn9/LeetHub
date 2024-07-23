class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        nums.sort(reverse=True)
        nums_count = Counter(nums)
        
        # Step 2: Sort nums based on two keys
        # First key: Frequency of the number (ascending order)
        # Second key: The number itself (descending order, hence the negative sign
        nums.sort(key=lambda x: (nums_count[x], -x))

        return nums
        