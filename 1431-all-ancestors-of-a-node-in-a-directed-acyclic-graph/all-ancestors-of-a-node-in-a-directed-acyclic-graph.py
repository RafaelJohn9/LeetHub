from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the graph and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * n
        for ancestor, descendant in edges:
            graph[ancestor].append(descendant)
            in_degree[descendant] += 1
        
        # List to store the ancestors of each node
        ancestors = [set() for _ in range(n)]
        
        # Topological sort using Kahn's algorithm
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            
            for descendant in graph[node]:
                ancestors[descendant].update(ancestors[node])
                ancestors[descendant].add(node)
                in_degree[descendant] -= 1
                if in_degree[descendant] == 0:
                    queue.append(descendant)
        
        # Convert sets to sorted lists
        result = [sorted(list(anc)) for anc in ancestors]
        
        return result
