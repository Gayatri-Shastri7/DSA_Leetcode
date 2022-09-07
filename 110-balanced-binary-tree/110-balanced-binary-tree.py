# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        b = [0]
        b[0] = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
                b[0] = False
            
            return max(left, right) + 1
        
        dfs(root)
        return b[0]
