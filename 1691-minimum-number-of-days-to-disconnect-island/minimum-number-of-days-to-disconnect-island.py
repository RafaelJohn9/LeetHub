class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x, y, grid, visited):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1 or visited[x][y]:
                return
            visited[x][y] = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(x + dx, y + dy, grid, visited)
        
        def is_disconnected():
            visited = [[False] * len(grid[0]) for _ in range(len(grid))]
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        if count > 0:  # More than one island found
                            return True
                        dfs(i, j, grid, visited)
                        count += 1
            return count != 1

        if is_disconnected():
            return 0  # Already disconnected

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Temporarily change land to water
                    if is_disconnected():
                        return 1
                    grid[i][j] = 1  # Revert the change

        return 2