from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(k: int, conditions: List[List[int]]) -> List[int]:
            indegree = {i: 0 for i in range(1, k+1)}
            graph = defaultdict(list)
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            zero_indegree = deque([node for node in range(1, k+1) if indegree[node] == 0])
            topo_order = []
            
            while zero_indegree:
                node = zero_indegree.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree.append(neighbor)
            
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {val: idx for idx, val in enumerate(row_order)}
        col_pos = {val: idx for idx, val in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for val in range(1, k+1):
            matrix[row_pos[val]][col_pos[val]] = val
        
        return matrix