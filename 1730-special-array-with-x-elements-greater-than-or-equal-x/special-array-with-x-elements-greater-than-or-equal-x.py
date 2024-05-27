class Solution:
    def specialArray(self, nums: List[int]) -> int:
       # Sort the array
        nums.sort()
        n = len(nums)
           
        # Iterate over possible values of x
        for x in range(n + 1):
            # Count how many numbers are greater than or equal to x
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
        
            # Check if count matches x
            if count == x:
                return x
    
        # If no special x is found
        return -1