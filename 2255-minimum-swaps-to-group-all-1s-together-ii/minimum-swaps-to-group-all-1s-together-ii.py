class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        If you use the Sliding Window technique
        and find the max numbers of ones in the windows
        you subtract it from total number of ones
        you have the min number of swaps needed
        """
        n: int = len(nums)

        total_ones: int = sum(nums)
        current_ones: int = sum(nums[:total_ones])
        max_ones: int =  current_ones

        # double to handle circular array property
        nums: int = nums + nums

        for i in range(1, n):
            current_ones += (-nums[i - 1] + nums[i + total_ones - 1])
            max_ones = max(max_ones, current_ones)
        
        print(total_ones, max_ones)
        return total_ones - max_ones