class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
            
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to find shortest paths between all pairs of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities within the distanceThreshold
        min_reachable_cities = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable_cities = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            if reachable_cities < min_reachable_cities or (reachable_cities == min_reachable_cities and i > best_city):
                min_reachable_cities = reachable_cities
                best_city = i
        
        return best_city
