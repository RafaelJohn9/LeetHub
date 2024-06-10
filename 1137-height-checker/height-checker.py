class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        count = 0

        for height, expected_height in zip(heights, expected):
            if height != expected_height:
                count += 1

        return count