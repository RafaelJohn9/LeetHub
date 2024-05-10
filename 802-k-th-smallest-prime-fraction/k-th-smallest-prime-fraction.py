from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction_size = {}
        n = len(arr)

        # Instead of converting the indices to string, directly store the fractions
        for i in range(n - 1):
            for j in range(i + 1, n):
                fraction_size[(i, j)] = arr[i] / arr[j]

        # Sort the fractions based on their values
        sorted_fractions = sorted(fraction_size.items(), key=lambda item: item[1])

        # Extract the kth smallest fraction
        kth_fraction_indices = sorted_fractions[k - 1][0]

        # Return the kth smallest fraction
        return [arr[kth_fraction_indices[0]], arr[kth_fraction_indices[1]]]
