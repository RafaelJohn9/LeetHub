from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize the transformation cost matrix
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        
        # Fill the transformation cost matrix with given transformations
        for i in range(26):
            dist[i][i] = 0
        
        for o, c, z in zip(original, changed, cost):
            dist[ord(o) - ord('a')][ord(c) - ord('a')] = min(dist[ord(o) - ord('a')][ord(c) - ord('a')], z)
        
        # Apply Floyd-Warshall algorithm to find all-pairs shortest path
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] < INF and dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate the minimum cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            cost_to_transform = dist[ord(s_char) - ord('a')][ord(t_char) - ord('a')]
            if cost_to_transform == INF:
                return -1
            total_cost += cost_to_transform
        
        return total_cost

