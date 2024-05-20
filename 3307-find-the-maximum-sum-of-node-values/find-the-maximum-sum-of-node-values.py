class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)

        deltas = []
        for x in nums:
            deltas.append((x ^ k) - x)
        
        deltas.sort(reverse=True)
        total = sum(nums)
        best = total

        i = 0

        while i + 1 < N:
            total += deltas[i]  + deltas[i + 1]
            best = max(best, total)
            i += 2
            
        return best