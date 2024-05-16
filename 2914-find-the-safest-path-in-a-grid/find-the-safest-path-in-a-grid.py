class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def bfs_from_thieves(grid):
            n = len(grid)
            distance = [[float('inf')] * n for _ in range(n)]
            queue = deque()

            # Initialize queue with all thieves' positions
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        distance[r][c] = 0

            # Perform multi-source BFS
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] == float('inf'):
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))

            return distance

        def can_reach_end_with_safeness(grid, min_safeness, distance):
            n = len(grid)
            if distance[0][0] < min_safeness:
                return False

            queue = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and distance[nx][ny] >= min_safeness:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

            return False
    
        n = len(grid)
        distance = bfs_from_thieves(grid)

        left, right = 0, min(n - 1, n - 1)
        while left < right:
            mid = (left + right + 1) // 2
            if can_reach_end_with_safeness(grid, mid, distance):
                left = mid
            else:
                right = mid - 1

        return left
