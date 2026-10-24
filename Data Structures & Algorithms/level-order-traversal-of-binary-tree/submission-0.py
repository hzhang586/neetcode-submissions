# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        level = [root]
        while level:
            new_level = []
            level_value = []
            for node in level:
                level_value.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            ans.append(level_value)

            level = new_level
        
        return ans
