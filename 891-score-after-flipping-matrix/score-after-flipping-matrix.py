class Solution:
    def matrixScore(self, grid):
        if not grid:
            return 0
        
        # Function to flip a row
        def flip(row):
            return [1 - digit for digit in row]

        # Ensure the first digit of each row is 1
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = flip(grid[i])

        # Flip columns if needed to maximize score
        for j in range(1, len(grid[0])):
            count_ones = sum(grid[i][j] for i in range(len(grid)))
            if count_ones < len(grid) / 2:
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate the total score
        total_score = 0
        for row in grid:
            total_score += int(''.join(map(str, row)), 2)

        return total_score

        