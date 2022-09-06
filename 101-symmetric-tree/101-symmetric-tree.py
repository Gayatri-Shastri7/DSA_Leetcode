# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None or root.right == None:
            return root.left == root.right
        if root.left.val != root.right.val:
            return False
        return self.isSymmetric(TreeNode(left=root.left.left, right=root.right.right)) and self.isSymmetric(TreeNode(left=root.left.right, right=root.right.left))

        