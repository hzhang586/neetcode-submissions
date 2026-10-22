"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        clones = dict()

        def dfs(n):
            if n in clones:
                return clones[n]
            
            new_n = Node(n.val)
            clones[n] = new_n
            for neigh in n.neighbors:
                new_n.neighbors.append(dfs(neigh))
            return new_n
    
        
        return dfs(node)