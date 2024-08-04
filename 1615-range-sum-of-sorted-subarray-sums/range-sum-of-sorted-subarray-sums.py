class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD: int = (10 ** 9) + 7

        # Generate subarrays sums
        subarrays_sums: List[int] = []
        for i in range(n):
            current_sum: int = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarrays_sums.append(current_sum)


        subarrays_sums.sort()
        result: int = 0

        return sum(subarrays_sums[left - 1: right]) % MOD