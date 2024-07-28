from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Step 1: Build the graph as an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: BFS initialization
        queue = [(1, 0)]  # (current_vertex, current_time)
        times = [[float('inf'), float('inf')] for _ in range(n + 1)]
        times[1][0] = 0
        
        while queue:
            curr, curr_time = queue.pop(0)
            
            # Determine if the current signal is red or green
            k = curr_time // change
            if k % 2 == 1:
                wait_time = change - (curr_time % change)
            else:
                wait_time = 0
            
            # Step 3: Explore all neighbors
            for neighbor in graph[curr]:
                new_time = curr_time + time + wait_time
                
                # Update the first and second minimum times to reach the neighbor
                if new_time < times[neighbor][0]:
                    times[neighbor][1] = times[neighbor][0]
                    times[neighbor][0] = new_time
                    queue.append((neighbor, new_time))
                elif times[neighbor][0] < new_time < times[neighbor][1]:
                    times[neighbor][1] = new_time
                    queue.append((neighbor, new_time))
        
        return times[n][1]
