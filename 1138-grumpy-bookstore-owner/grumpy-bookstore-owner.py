class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Total customers satisfied without any changes in grumpiness
        total_satisfied = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                total_satisfied += customers[i]
        
        # Compute the extra satisfaction we can gain by suppressing grumpiness for 'minutes' duration
        extra_satisfied = 0
        max_extra_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i]:
                extra_satisfied += customers[i]
            # If we have passed the window size, subtract the element that goes out of the window
            if i >= minutes and grumpy[i - minutes]:
                extra_satisfied -= customers[i - minutes]
            # Track the maximum extra satisfaction possible within any window of 'minutes' duration
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return total_satisfied + max_extra_satisfied