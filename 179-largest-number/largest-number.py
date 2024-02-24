class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        
        # Custom comparison function for sorting
        def sorting_order(x, y):
            return int(y + x) - int(x + y)
             
        # Sort numbers using the custom comparison function
        nums_str.sort(key=cmp_to_key(sorting_order))
        
        # Concatenate the sorted numbers
        result = ''.join(nums_str)
        
        # Handle leading zeros
        result = result.lstrip('0') or '0'
        
        return result