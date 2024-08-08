class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # East, South West, North
        directions: List[Tuple[int]] = [(0, 1), [1, 0], (0, -1), (-1, 0)]

        result: List[List[int]] = []
        direction_step: int = 0 # we begin going East
        total_cells: int = rows * cols
        step: int = 1
        r, c = rStart, cStart

        result.append([r,c])

        while len(result) < total_cells:
            for _ in range(2):  # twice per interval
                dr, dc = directions[direction_step]
                for _ in range(step):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r,c])
                    
                direction_step = (direction_step + 1) % 4
            step += 1
        
        return result

                    
