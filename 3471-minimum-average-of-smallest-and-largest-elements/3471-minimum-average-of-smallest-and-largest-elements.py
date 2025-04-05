class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()  # Sort the array
        averages = []
        
        # Iterate over the array n / 2 times
        n = len(nums)
        for i in range(n // 2):
            min_element = nums[i]  # Smallest element (at the front)
            max_element = nums[n - 1 - i]  # Largest element (at the end)
            avg = (min_element + max_element) / 2  # Average of min and max
            averages.append(avg)
        
        return min(averages)  # Return the minimum element in averages
