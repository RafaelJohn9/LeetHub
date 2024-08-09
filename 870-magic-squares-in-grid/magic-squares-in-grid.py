class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row_length: int = len(grid)
        col_length: int = len(grid[0])
        total_cells: int = row_length * col_length

        # directions to traverse
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_step = directions[0]

        if total_cells < 9:
            return 0

        def is_magic_square(coordinate: List[int]) -> bool:
            """ check if it is a magic square
            from the coord """
            curr_row, curr_col = coordinate
            c_r = curr_row
            c_l = curr_col

            if (curr_row + 3) > row_length \
                or (curr_col + 3) > col_length:
                return False

            result = [
                grid[curr_row][curr_col: curr_col + 3],
                grid[curr_row + 1][curr_col: curr_col + 3],
                grid[curr_row + 2][curr_col: curr_col + 3]
            ]

            validating_set = set()
            for row in result:
                for num in row:
                    if num > 0 and num <= 9:
                        validating_set.add(num)

            if len(validating_set) != 9:
                return False


            # deal with diagonals
            l_diag = (grid[curr_row][curr_col] + grid[curr_row + 1][curr_col + 1] + grid[curr_row + 2][curr_col+ 2])
            r_diag = (grid[curr_row][curr_col + 2] + grid[curr_row + 1][curr_col + 1] + grid[curr_row + 2][curr_col])
            diagonals = l_diag == r_diag

            # deal with columns
            first_col = grid[curr_row][curr_col] + grid[curr_row + 1][curr_col] + grid[curr_row + 2][curr_col]
            second_col = grid[curr_row][curr_col + 1] + grid[curr_row + 1][curr_col + 1] + grid[curr_row + 2][curr_col + 1]
            third_col = grid[curr_row][curr_col + 2] + grid[curr_row + 1][curr_col + 2] + grid[curr_row + 2][curr_col + 2]
            columns = first_col == second_col == third_col

            # deal with rows
            first_row = sum(result[0])
            second_row = sum(result[1])
            third_row = sum(result[2])
            rows = first_row == second_row == third_row
 
            if columns == diagonals == rows:
                return l_diag == first_col == first_row
            else:
                return False
        
        ans: int = 0
        for  row in range(row_length - 2):
            for col in range(col_length - 2):
                if is_magic_square([row, col]):
                    ans += 1
        
        return ans