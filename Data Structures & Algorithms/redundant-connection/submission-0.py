class unionFind:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return True
        if self.size[root_x] < self.size[root_y]:
            root_x,root_y = root_y,root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return False
            

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        uf = unionFind(n)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            if uf.union(u,v):
                return edge
            