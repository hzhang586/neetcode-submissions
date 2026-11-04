class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self,x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []

        # Step 1: Construct all edges
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                weight = abs(x1-x2) + abs(y1-y2)
                edges.append((weight, i, j))
        
        # Step2: Sort edges by weight
        edges.sort()
        
        # Step3: Kruskal + Union-Find

        uf = UnionFind(n)
        total_cost = 0
        edge_count = 0

        for weight, u, v in edges:
            if uf.union(u,v):
                total_cost += weight
                edge_count += 1
            
            if edge_count == n-1:
                break
        
        return total_cost