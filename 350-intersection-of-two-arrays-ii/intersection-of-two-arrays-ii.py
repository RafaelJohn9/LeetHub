class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a dictionary to count occurrences of each element in nums1
        counts = {}
    
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
    
        # List to store the result
        result = []
    
        # Iterate through nums2 and collect common elements
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1
    
        return result
