# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = list()
        nums = set()
        
        if root.left: stack.append(root.left) 
        if root.right: stack.append(root.right) 
        nums.add(root.val)

        while stack:
            node = stack.pop(-1)
            if k - node.val in nums: return True
            if node.left: stack.append(node.left) 
            if node.right: stack.append(node.right) 
            nums.add(node.val)
