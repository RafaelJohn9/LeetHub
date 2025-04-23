from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Coordinate compression: Create a sorted list of unique instructions
        sorted_instructions = sorted(set(instructions))
        
        # Map each element in instructions to its compressed index
        compress = {value: idx + 1 for idx, value in enumerate(sorted_instructions)}  # 1-based index
        
        # Fenwick Tree to track counts of numbers
        class FenwickTree:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)

            def update(self, index, value):
                while index <= self.n:
                    self.tree[index] += value
                    index += index & -index

            def query(self, index):
                result = 0
                while index > 0:
                    result += self.tree[index]
                    index -= index & -index
                return result
        
        # Initialize Fenwick Tree
        ft = FenwickTree(len(sorted_instructions))
        
        total_cost = 0
        for num in instructions:
            # Get the compressed index of num
            idx = compress[num]
            
            # Cost calculation:
            # Count of elements strictly less than num
            left = ft.query(idx - 1)
            # Count of elements strictly greater than num
            right = ft.query(len(sorted_instructions)) - ft.query(idx)
            
            # Cost is the minimum of these two counts
            cost = min(left, right)
            total_cost = (total_cost + cost) % MOD
            
            # Insert current number into the Fenwick Tree
            ft.update(idx, 1)
        
        return total_cost
