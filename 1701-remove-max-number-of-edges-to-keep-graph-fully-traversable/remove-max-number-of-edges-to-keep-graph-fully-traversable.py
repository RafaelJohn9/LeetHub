from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        common_edges = 0
        removed_edges = 0

        # First pass for type 3 edges (usable by both Alice and Bob)
        for edge_type, start, end in edges:
            if edge_type == 3:
                if alice.union(start - 1, end - 1):
                    bob.union(start - 1, end - 1)
                    common_edges += 1
                else:
                    removed_edges += 1
        
        # Second pass for type 1 and type 2 edges
        for edge_type, start, end in edges:
            if edge_type == 1:
                if not alice.union(start - 1, end - 1):
                    removed_edges += 1
            elif edge_type == 2:
                if not bob.union(start - 1, end - 1):
                    removed_edges += 1

        # Check if both Alice and Bob can traverse the entire graph
        if alice.components != 1 or bob.components != 1:
            return -1
        
        return removed_edges