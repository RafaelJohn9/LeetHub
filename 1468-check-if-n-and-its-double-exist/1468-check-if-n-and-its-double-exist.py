class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # Use a set for O(1) lookup time
        
        zero_count = arr.count(0)  # Count zeros once
        if zero_count > 1:
            return True  # If there are at least two zeros, return True
        
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        
        return False