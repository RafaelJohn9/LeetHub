class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []

        for i in range(1, len(grid) - 1):
            row_in_maxLocal = []
            for j in range(1, len(grid[0]) - 1):
                max_num = float('-inf')
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        max_num = max(max_num, grid[r][c])
                row_in_maxLocal.append(max_num)
            maxLocal.append(row_in_maxLocal)
        return maxLocal
