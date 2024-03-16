class Solution:
    def set_row_zero(self, matrix, coordinate):
        """
        sets an entire row to zero
        """
        x,y = coordinate
        # left first
        for i in range(y - 1, -1, -1):
            matrix[x][i] = 0

        # right
        for j in range(y + 1, len(matrix[0])):
            matrix[x][j] = 0 

    def set_column_zero(self, matrix, coordinate):
        """
        sets an entire column to zero
        """
        x,y = coordinate
        # top first
        for i in range(x - 1, -1, -1):
            matrix[i][y] = 0
        # down
        for j in range(x + 1, len(matrix)):
            matrix[j][y] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        add a backtrack that checks if element was initially zero
        """
        backtrack = {}
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                backtrack[str([x, y])] = matrix[x][y]
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if backtrack[str([x, y])] == 0:
                    self.set_row_zero(matrix, [x, y])
                    self.set_column_zero(matrix, [x, y])
