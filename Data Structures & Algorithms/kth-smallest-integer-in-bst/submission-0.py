# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        ans = -1

        def dfs(root):
            nonlocal counter
            nonlocal ans

            if not root:
                return
            
            dfs(root.left)
            if ans != -1:
                return
            counter += 1
            if counter == k:
                ans = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return ans
            
        