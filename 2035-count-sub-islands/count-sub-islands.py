class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> bool:
            # If out of bounds or in water
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            
            # Mark the current cell as visited in grid2
            grid2[i][j] = 0
            
            # Check if this part of grid2 is a sub-island part in grid1
            is_sub_island = grid1[i][j] == 1
            
            # Visit all 4 possible directions (up, down, left, right)
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i, j + 1)
            is_sub_island &= dfs(i, j - 1)
            
            return is_sub_island
        
        # Initialize the sub-island count
        sub_island_count = 0
        
        # Iterate through each cell in grid2
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                # Start DFS if we find an island part in grid2
                if grid2[i][j] == 1:
                    # If the DFS confirms it as a sub-island, increase the count
                    if dfs(i, j):
                        sub_island_count += 1
                        
        return sub_island_count
