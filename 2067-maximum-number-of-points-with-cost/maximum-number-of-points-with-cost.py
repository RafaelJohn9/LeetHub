class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        returns the max score one can get with cost
        Where cost is difference between prev and current columns
        """
        n: int = len(points)
        m: int = len(points[0])
        a: List[int] = points[0].copy()

        for i in range(n - 1):
            b = [a[0]]
            
            for j in range(1, m):
                b.append(max(b[-1] - 1, a[j]))
            
            for j in range(m - 2, -1, -1):
                b[j] = max(b[j], b[j + 1] - 1)
            
            for j in range(m):
                a[j] = b[j] + points[i + 1][j]
        
        return max(a)