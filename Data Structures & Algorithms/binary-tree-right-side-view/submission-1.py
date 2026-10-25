# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        level = [root]
        ans = []
        while level:
            ans.append(level[0].val)
            new_level = []
            for node in level:
                if node.right:
                    new_level.append(node.right)
                if node.left:
                    new_level.append(node.left)
            level = new_level
        
        return ans
        