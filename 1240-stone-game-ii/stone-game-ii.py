class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Cache for storing the maximum stones Alice can get starting from index i with a given M
        dp = {}

        # Suffix sums to efficiently calculate the remaining stones
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Helper function to compute the maximum stones Alice can get
        def max_stones(i, M):
            # If all piles are taken, return 0
            if i >= n:
                return 0
            # If the result is already computed, return it
            if (i, M) in dp:
                return dp[(i, M)]
            
            # Alice can take between 1 and 2M piles
            max_stones_alice_can_take = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:  # Prevent taking more piles than are available
                    break
                # Calculate the stones Alice gets by taking X piles, minus the stones Bob gets after
                max_stones_alice_can_take = max(
                    max_stones_alice_can_take,
                    suffix_sum[i] - max_stones(i + X, max(M, X))
                )
            
            # Cache the result before returning
            dp[(i, M)] = max_stones_alice_can_take
            return max_stones_alice_can_take

        # Alice starts with the first pile and M = 1
        return max_stones(0, 1)
