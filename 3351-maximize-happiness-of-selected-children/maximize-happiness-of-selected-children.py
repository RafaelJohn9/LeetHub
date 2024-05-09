class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness.sort(reverse=True)

        subtract = 0
        total = 0
        for i in range(k):
            total += happiness[i] - subtract if happiness[i] > subtract else 0
            subtract += 1
        
        return total
