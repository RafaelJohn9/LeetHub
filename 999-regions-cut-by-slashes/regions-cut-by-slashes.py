from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n: int = len(grid)

        # expand grid to avoid counting mistake
        expanded_grid: List[List[int]] = [[0] * (n * 3) for _ in range(n * 3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[i * 3][j * 3 + 2] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[i * 3][j * 3] = 1
                    expanded_grid[i * 3 + 1][j * 3 + 1] = 1
                    expanded_grid[i * 3 + 2][j * 3 + 2] = 1

        # dfs covers counted spaces with 1
        def dfs(x, y):
            if x < 0 or x >= n * 3 or y < 0 or y >= n * 3 or expanded_grid[x][y] != 0:
                return
            
            expanded_grid[x][y] = 1
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        regions: int = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if expanded_grid[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions