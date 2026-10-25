# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return float('-inf')
            
            max_left = dfs(node.left)
            max_right = dfs(node.right)
            max_cur = max(max_left+node.val,max_right+node.val,max_left+max_right+node.val,node.val)
            ans = max(max_cur,ans)
            return max(max_left+node.val,max_right+node.val,node.val)
        
        dfs(root)
        return ans

