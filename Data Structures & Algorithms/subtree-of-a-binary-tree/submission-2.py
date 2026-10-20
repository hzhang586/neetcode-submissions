# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def isSameTree(p,q):
            if not p or not q:
                return p is q
            
            if p.val != q.val:
                return False
            
            if not isSameTree(p.left,q.left):
                return False
            
            if not isSameTree(p.right,q.right):
                return False
            
            return True
        
        if root is None:
            return False
        if subRoot is None:
            return False
        
        if isSameTree(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        if left:
            return True
        right = self.isSubtree(root.right,subRoot)
        return right