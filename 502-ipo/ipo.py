from heapq import heappush, heappop
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of (capital, profit) pairs
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        
        # Min-heap to store projects based on required capital
        min_heap = []
        for c, p in projects:
            heappush(min_heap, (c, p))
        
        # Max-heap to store profits of the projects that can be undertaken
        max_heap = []
        
        # Execute up to k projects
        for _ in range(k):
            # Move all projects that can be started with current capital to the max-heap
            while min_heap and min_heap[0][0] <= w:
                c, p = heappop(min_heap)
                heappush(max_heap, -p)  # Use negative to simulate max-heap
            
            # If no more projects can be started, break
            if not max_heap:
                break
            
            # Start the project with the maximum profit
            w += -heappop(max_heap)
        
        return w