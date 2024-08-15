class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        old_row: List[int] = [1] * n

        for i in range(m - 1):
            new_row: List[int] = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + old_row[j]
            old_row = new_row

        return old_row[0]