"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        clones = dict()

        def dfs(node):
            if node is None:
                return None
            if node in clones:
                return clones[node]
            
            new_node = Node(node.val)
            clones[node] = new_node

            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)
            
            return new_node
        
        return dfs(head)
