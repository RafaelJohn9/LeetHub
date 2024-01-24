class Solution:
    def countBits(self, n: int) -> List[int]:
        onesList = []
        for i in range(n + 1):
            a = bin(i)
            onesList.append(int(a.count('1')))
        return onesList