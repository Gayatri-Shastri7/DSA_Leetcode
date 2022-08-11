# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vbst(root, low, high):
            if root is None:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return vbst(root.left, low, root.val) and vbst(root.right, root.val, high)
        
        return vbst(root, -math.inf, math.inf)
