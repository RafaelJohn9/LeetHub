class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = list(map(lambda x : x ** 2, nums))
        result.sort()
        return result