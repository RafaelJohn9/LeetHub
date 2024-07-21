class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the matrix with zeros
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        # Greedy algorithm to fill the matrix
        for i in range(m):
            for j in range(n):
                # Determine the value to place in the current cell
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                
                # Update the row and column sums
                rowSum[i] -= value
                colSum[j] -= value
                
                # If row sum or column sum becomes zero, continue to the next cell
                # instead of breaking out of the loop
                
        return matrix