class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Union-Find (Disjoint Set Union) helper functions
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Union stones by their rows and columns
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if ~y not in parent:  # ~y is used to distinguish between rows and columns
                parent[~y] = ~y
            union(x, ~y)

        # Count how many unique connected components there are
        return len(stones) - len({find(x) for x in parent})
