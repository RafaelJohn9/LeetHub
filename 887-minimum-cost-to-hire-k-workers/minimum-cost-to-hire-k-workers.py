class Solution:
    import heapq
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate ratios
        ratios = [(w / q, w, q) for w, q in zip(wage, quality)]
        ratios.sort()
        
        min_cost = float('inf')
        sum_quality = 0
        max_heap = []
        
        for ratio, w, q in ratios:
            heapq.heappush(max_heap, -q)
            sum_quality += q
            
            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)
        
        return min_cost