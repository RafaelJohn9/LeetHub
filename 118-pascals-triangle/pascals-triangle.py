class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        
        # BASECASES
        pascal.append([1])
        pascal.append([1, 1])

        if numRows <= 2:
            return pascal[:numRows]
        
        for row in range(2, numRows):
            previousRow = pascal[row - 1]
            i = 0
            nextRow = []
            nextRow.append(previousRow[i])
            i += 1
            while i < len(previousRow):
                nextRow.append(previousRow[i - 1] + previousRow[i])
                i += 1
            nextRow.append(previousRow[-1])
            pascal.append(nextRow)
        return pascal