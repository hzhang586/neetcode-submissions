# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(node):
            nonlocal max_diam

            if node is None:
                return 0
            
            left_max_dist = 1 + dfs(node.left) if node.left else 0
            right_max_dist = 1+ dfs(node.right) if node.right else 0

            if left_max_dist + right_max_dist > max_diam:
                max_diam = left_max_dist + right_max_dist
            
            return max(left_max_dist,right_max_dist)
        
        root_depth = dfs(root)
        
        return root_depth if root_depth > max_diam else max_diam
            



        