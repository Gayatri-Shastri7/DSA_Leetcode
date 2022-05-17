# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return cloned
        if cloned.val == target.val:
            return cloned
        a = self.getTargetCopy(original, cloned.left, target)
        if a is not None:
            return a
        else:
            return self.getTargetCopy(original, cloned.right, target)
