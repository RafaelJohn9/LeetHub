class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def is_valid(subset, num):
            for existing in subset:
                if abs(existing - num) == k:
                    return False
            return True
        
        def backtrack(start, current):
            nonlocal count
            if start > len(nums):
                return
            count += 1
            for i in range(start, len(nums)):
                if is_valid(current, nums[i]):
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()

        nums.sort()  # Sort the list to handle subsets in an ordered way
        count = -1  # Initialize count (-1 to exclude the empty subset)
        backtrack(0, [])
        return count